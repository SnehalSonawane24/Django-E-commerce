from rest_framework import generics, viewsets, status
from ecommerce.models import User, Product, Order
from ecommerce.serializers import  UserSignupSerializer, ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics, viewsets
from .models import User, Product, Order
from .serializers import  UserSignupSerializer, ProductSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny


class CustomResponseMixin:
    def success_response(self, data, message="Success", status_code=status.HTTP_200_OK):
        return Response({
            "success": True,
            "message": message,
            "data": data
        }, status=status_code)

    def error_response(self, message="Error", status_code=status.HTTP_400_BAD_REQUEST):
        return Response({
            "success": False,
            "message": message,
            "data": None
        }, status=status_code)
    

class SignupView(CustomResponseMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return self.success_response(serializer.data, message="User registered successfully", status_code=201)
        return self.error_response(serializer.errors)


class ProductViewSet(CustomResponseMixin, viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == 'retailer':
            return Product.objects.filter(retailer=user)
        return Product.objects.all()

    def perform_create(self, serializer):
        serializer.save(retailer=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return self.success_response(serializer.data, message="Product created successfully", status_code=201)
        return self.error_response(serializer.errors)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.success_response(serializer.data, message="Product list fetched successfully")

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.success_response(serializer.data, message="Product retrieved successfully")


class OrderViewSet(CustomResponseMixin, viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'customer':
            return Order.objects.filter(customer=user)
        return Order.objects.all()

    def perform_create(self, serializer):
        customer = self.request.user
        products = self.request.data.get('products', [])
        product_objects = Product.objects.filter(id__in=products)
        total_price = sum(product.price for product in product_objects)
        serializer.save(customer=customer, total_price=total_price)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return self.success_response(serializer.data, message="Order placed successfully", status_code=201)
        return self.error_response(serializer.errors)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return self.success_response(serializer.data, message="Order list fetched successfully")
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return self.success_response(serializer.data, message="Order updated successfully")
        return self.error_response(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return self.success_response({}, message="Order deleted successfully", status_code=204)