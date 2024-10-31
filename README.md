# E-commerce Online Platform

## 📦 Project Overview
This project is an E-commerce platform backend developed using Django REST framework. It includes user authentication, product management, stock management, and category management features. The backend connects to a PostgreSQL database managed via pgAdmin4.

## 🚀 Features
- User Authentication (Login, Registration, Logout)
- Product Management (CRUD operations)
- Stock Management (CRUD operations)
- Category Management (CRUD operations)

## 🛠️ Technologies Used
- Django
- Django REST Framework
- PostgreSQL
- pgAdmin4

## 📁 Project Structure
E-commerce Online Platform/ │ ├── e_commerce/ # Main Django project folder │ ├── init.py # Package initialization │ ├── settings.py # Project settings │ ├── urls.py # Project URLs │ ├── wsgi.py # WSGI entry point │ └── ... │ ├── products/ # App for product management │ ├── migrations/ # Database migrations │ ├── admin.py # Admin configurations │ ├── models.py # Product, Stock, and Category models │ ├── serializers.py # Serializers for models │ ├── views.py # API views │ ├── urls.py # App URLs │ └── ... │ ├── users/ # App for user management │ ├── migrations/ # Database migrations │ ├── admin.py # Admin configurations │ ├── models.py # User models │ ├── serializers.py # Serializers for models │ ├── views.py # API views │ ├── urls.py # App URLs │ └── ... │ ├── requirements.txt # Project dependencies └── db.sql # SQL file for database schema

## 📥 Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- pgAdmin4

### Step 1: Clone the Repository
  git clone <repository-url>
  cd e-commerce-online-platform
### Step 2: Create a Virtual Environment
python -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
### Step 3: Install Requirements
  pip install -r requirements.txt
## 📦 Step 4: Setup PostgreSQL

### Create a Database:
1. Open **pgAdmin4**.
2. Right-click on **"Databases"** > **"Create"** > **"Database"**.
3. Name the database (e.g., `ecommerce_db`).

### Execute SQL Script:
1. Open the **SQL editor** in pgAdmin4.
2. Load the `db.sql` file provided in the project folder.
3. Execute the script to create the required tables.


## ⚙️ Step 5: Update Django Settings

In e_commerce/settings.py, update the DATABASES configuration:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ecommerce_db',  # your database name
        'USER': 'your_username',  # your PostgreSQL username
        'PASSWORD': 'your_password',  # your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',  # default PostgreSQL port
    }
}

### Instructions:
- Replace `your_username` and `your_password` with your actual PostgreSQL credentials.
- This format maintains clarity and organization, making it easy to follow.
# 🛠️ Running the Project

Here’s your content formatted in Markdown:

```markdown
# 🛠️ Running the Project

## Step 1: Apply Migrations
```bash
python manage.py migrate
```

## Step 2: Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```

## Step 3: Run the Development Server
```bash
python manage.py runserver

# The server will start at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

# 📡 API Endpoints

## User Endpoints
- **User Registration:** `POST` [http://127.0.0.1:8000/user/register/](http://127.0.0.1:8000/user/register/)
- **User Login:** `POST` [http://127.0.0.1:8000/user/login/](http://127.0.0.1:8000/user/login/)
- **User Logout:** `POST` [http://127.0.0.1:8000/user/logout/](http://127.0.0.1:8000/user/logout/)
- **List Users:** `GET` [http://127.0.0.1:8000/user/list/](http://127.0.0.1:8000/user/list/)

## Product Endpoints
- **List Products:** `GET` [http://127.0.0.1:8000/product/products/](http://127.0.0.1:8000/product/products/)
- **Create Product:** `POST` [http://127.0.0.1:8000/product/products/](http://127.0.0.1:8000/product/products/)
- **Update Product:** `PUT` [http://127.0.0.1:8000/product/products/<id>/](http://127.0.0.1:8000/product/products/<id>/)
- **Delete Product:** `DELETE` [http://127.0.0.1:8000/product/products/<id>/](http://127.0.0.1:8000/product/products/<id>/)

## Stock Endpoints
- **List Stocks:** `GET` [http://127.0.0.1:8000/product/stocks/](http://127.0.0.1:8000/product/stocks/)
- **Create Stock:** `POST` [http://127.0.0.1:8000/product/stocks/](http://127.0.0.1:8000/product/stocks/)
- **Update Stock:** `PUT` [http://127.0.0.1:8000/product/stocks/<id>/](http://127.0.0.1:8000/product/stocks/<id>/)
- **Delete Stock:** `DELETE` [http://127.0.0.1:8000/product/stocks/<id>/](http://127.0.0.1:8000/product/stocks/<id>/)

## Category Endpoints
- **List Categories:** `GET` [http://127.0.0.1:8000/category/categories/](http://127.0.0.1:8000/category/categories/)
- **Create Category:** `POST` [http://127.0.0.1:8000/category/categories/](http://127.0.0.1:8000/category/categories/)
- **Update Category:** `PUT` [http://127.0.0.1:8000/category/categories/<id>/](http://127.0.0.1:8000/category/categories/<id>/)
- **Delete Category:** `DELETE` [http://127.0.0.1:8000/category/categories/<id>/](http://127.0.0.1:8000/category/categories/<id>/)

# 🔍 Testing the API
You can test the API using tools like Postman or cURL. Make sure to set the appropriate headers (e.g., `Content-Type: application/json`) and include any required authentication tokens.


