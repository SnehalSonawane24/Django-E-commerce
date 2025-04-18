﻿# Django-E-commerce

###### A simple Django REST Framework-based backend for an E-commerce system. This project allows users to register as customers or retailers. Retailers can add products, and customers can place orders for products. The API supports authentication using JWT and provides CRUD operations for Users, Products, and Orders with role-based access control.

### Features
#### 🔐 JWT-based authentication using SimpleJWT

#### 👤 Role-based user handling: customer and retailer

#### 📦 Retailers can create and manage products

#### 🛒 Customers can place, update, and delete orders

#### 📋 Standardized API responses (success/error formats)

#### ✅ Secure endpoints (authentication required for most operations)


## 🛠️ Setup Instructions
1. Clone the repo
git clone https://github.com/SnehalSonawane24/Django-E-commerce.git

2. Create a virtual environment and activate it
python -m venv venv
#### Windows
venv\Scripts\activate
#### macOS/Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Apply migrations
python manage.py migrate

5. Create a superuser (for admin access)
python manage.py createsuperuser

6. Run the development server
python manage.py runserver


### Endpoints

## Retailer Sign Up

### Method
POST
### Endpoint
http://127.0.0.1:8000/api/signup/
### Payload
{
  "username": "snehal123",
  "email": "snehal@gmail.com",
  "password": "password123",
  "role": "retailer"
}
### Response
{
    "success": true,
    "message": "User registered successfully",
    "data": {
        "username": "snehal123",
        "email": "snehal@gmail.com",
        "role": "retailer"
    }
}


## Retailer Sign Up

### Method
POST
### Endpoint
http://127.0.0.1:8000/api/signup/
### Payload
{
  "username": "admin123",
  "email": "admin@gmail.com",
  "password": "password123",
  "role": "customer"
}
### Response
{
    "success": true,
    "message": "User registered successfully",
    "data": {
        "username": "hello123",
        "email": "hello@gmail.com",
        "role": "retailer"
    }
}


## User Login

### Method
POST
### Endpoint
http://127.0.0.1:8000/api/login/
### Payload
{
  "username": "snehal123",
  "password": "password123"
}
### Response
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NDk5MTI2MSwiaWF0IjoxNzQ0OTA0ODYxLCJqdGkiOiJiNTYyMTUzZmE4MGI0MTMyYjg5OTFjM2Y1YTY5NzBjNyIsInVzZXJfaWQiOjF9.S5SUqliaCT-4EDmtLFPYf8qSG6tNivnKp_0l7siDPeE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0OTA1MTYxLCJpYXQiOjE3NDQ5MDQ4NjEsImp0aSI6IjU3MDgwZTFiNGIwZjRjNzk5ZWUwOGQzNWIyYzY3YTYxIiwidXNlcl9pZCI6MX0.fq0xEF6h0PxemQaG6jmMI5tvh8_8oz-3vE_MNvXDp1E"
}


## Create Product 

### Method
POST
### Endpoint
http://127.0.0.1:8000/api/products/
### Payload
{
  "name": "iPhone 15",
  "description": "Latest Apple smartphone",
  "price": 120000,
  "stock": 25
}
### Header
Authorization: Bearer <access_token>
### Response
{
    "success": true,
    "message": "Product created successfully",
    "data": {
        "id": 3,
        "name": "iPhone 15",
        "description": "Latest Apple smartphone",
        "price": "120000.00",
        "stock": 25,
        "retailer": 1,
        "created_at": "2025-04-17T15:49:51.502728Z"
    }
}


## Product List

### Method
GET
### Endpoint
http://127.0.0.1:8000/api/products/
### Header
Authorization: Bearer <access_token>
### Response
{
    "success": true,
    "message": "Product list fetched successfully",
    "data": [
        {
            "id": 1,
            "name": "Samsung Galaxy S23",
            "description": "Flagship phone by Samsung",
            "price": "74999.00",
            "stock": 30,
            "retailer": 2,
            "created_at": "2025-04-17T14:14:29.867180Z"
        },
        {
            "id": 2,
            "name": "iPhone 15",
            "description": "Latest Apple smartphone",
            "price": "120000.00",
            "stock": 25,
            "retailer": 2,
            "created_at": "2025-04-17T14:23:52.314872Z"
        },
        {
            "id": 3,
            "name": "iPhone 15",
            "description": "Latest Apple smartphone",
            "price": "120000.00",
            "stock": 25,
            "retailer": 1,
            "created_at": "2025-04-17T15:49:51.502728Z"
        }
    ]
}


## Placed Order

### Method
POST
### Endpoint
http://127.0.0.1:8000/api/orders/
### Payload
{
  "products": [1],
  "status": "PENDING"
}
### Header
Authorization: Bearer <access_token>
### Response
{
    "success": true,
    "message": "Order placed successfully",
    "data": {
        "customer_name": "snehal123",
        "products": [
            1
        ],
        "total_price": "74999.00",
        "status": "PENDING"
    }
}


## Order List

### Method
GET
### Endpoint
http://127.0.0.1:8000/api/orders/
### Header
Authorization: Bearer <access_token>
### Response
{
    "success": true,
    "message": "Order list fetched successfully",
    "data": [
        {
            "customer_name": "snehal123",
            "products": [
                1
            ],
            "total_price": "74999.00",
            "status": "PENDING"
        },
        {
            "customer_name": "snehal123",
            "products": [
                1
            ],
            "total_price": "74999.00",
            "status": "PENDING"
        }
    ]
}


## Order Delete

### Method
DELETE
### Endpoint
http://127.0.0.1:8000/api/orders/
### Header
Authorization: Bearer <access_token>
### Response
{
    "success": true,
    "message": "Order deleted successfully",
    "data": [
        {
            "customer_name": "snehal123",
            "products": [
                1
            ],
            "total_price": "74999.00",
            "status": "PENDING"
        }
    ]
}


## Order update

### Method
PUT
### Endpoint
http://127.0.0.1:8000/api/orders/1/
### Payload
{
  "products": [2],
  "status": "PENDING"
}
### Header
Authorization: Bearer <access_token>
### Response
{
    "success": true,
    "message": "Order updated successfully",
    "data": {
        "customer_name": "snehal123",
        "products": [
            2
        ],
        "total_price": "74999.00",
        "status": "PENDING"
    }
}
