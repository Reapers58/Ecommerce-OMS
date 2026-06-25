# E-Commerce Order Management System (OMS)

## Overview

A backend E-Commerce Order Management System built with FastAPI, PostgreSQL, SQLAlchemy, Alembic, Docker, and JWT Authentication.

The project provides APIs for authentication, categories, products, cart management, orders, payments, wishlist, and reviews.

---

## Tech Stack

* Python 3
* FastAPI
* PostgreSQL
* SQLAlchemy 2.0
* Alembic
* Docker
* Pydantic v2
* pgAdmin
* JWT Authentication
* Passlib/Argon2 Password Hashing
* Uvicorn

---

## Features

### Authentication

* User Signup
* User Login
* JWT Token Generation
* User Profile
* Change Password

### Categories

* Create Category
* Get Categories
* Update Category
* Delete Category

### Products

* Create Product
* Get Products
* Search Products
* Filter by Category
* Filter by Brand
* Pagination
* Sorting

### Product Images

* Upload Product Images
* View Product Images

### Cart

* Add To Cart
* Get Cart
* Remove Items
* Clear Cart

### Orders

* Create Order
* Get Orders
* Update Order Status
* Cancel Orders

### Payments

* Create Payment
* Get Payments

### Wishlist

* Add To Wishlist
* Get Wishlist
* Remove Wishlist Items

### Reviews

* Create Review
* Get Reviews
* Delete Reviews

### Coupons

* Create Coupons
* Apply Coupons
* Update Coupons
* Delete Coupons

### Dashboard

* Admin Dashboard
* Seller Dashboard
* Customer Dashboard
* Low Stock Products
* Top Selling Products
* Recent Orders

---

## Project Structure

```text
Ecommerce-OMS
│
├── alembic/              # Database migrations
├── config/               # Application configuration
├── db/                   # Database utilities
├── media/                # Media storage
├── shared/               # Shared utilities
├── src/
│   ├── auth/             # Authentication module
│   ├── cart/             # Cart module
│   ├── categories/       # Category management
│   ├── coupons/          # Coupon module
│   ├── dashboard/        # Dashboard module
│   ├── models/           # SQLAlchemy models
│   ├── orders/           # Order management
│   ├── payments/         # Payment management
│   ├── product_images/   # Product image module
│   ├── products/         # Product management
│   ├── reviews/          # Product reviews
│   ├── sellers/          # Seller module
│   ├── users/            # User module
│   ├── wishlist/         # Wishlist module
│   ├── config.py
│   ├── database.py
│   └── router.py
│
├── .env
├── .env.example
├── .gitignore
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── main.py
├── README.md
└── requirements.txt
```


---

## Installation

### Clone Repository

```bash
git clone https://github.com/Reapers58/Ecommerce-OMS.git
cd Ecommerce-OMS
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt

```
### Start PostgreSQL using Docker

```bash
docker compose up -d

```

### Run Application

```bash
python -m uvicorn main:app --reload
```

---

## API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Database

PostgreSQL is used as the primary database and is managed using Docker and Alembic migrations.

---

## Author

Reaper
