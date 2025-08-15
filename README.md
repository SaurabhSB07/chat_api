# Django REST Framework Complete Authentication & AI Chat API with Simple JWT

This project is a solution to a technical assignment for building REST APIs for an AI chat system using Django and Django REST Framework. It demonstrates comprehensive user authentication and token-based access control integrated with a simple AI chat system.

---

## Assignment Overview

You were tasked with building REST APIs that allow users to:

- Register with a unique username and password.
- Log in and receive an authentication token.
- Chat with an AI-powered bot that deducts tokens per query.
- Check token balances.

The system manages user tokens, deducting 100 tokens per chat message, and saves chat history.

---

## Project Features

- *Custom User Model* with token management.
- *User Registration* API with username uniqueness and initial token allocation.
- *User Login* API using JWT tokens for secure authentication.
- *Chat API* with token deduction and chat history persistence.
- *Token Balance API* giving users access to their remaining token count.
- *Postman Collection* for API testing.

---

## Models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
tokens = models.IntegerField(default=4000)

class Chat(models.Model):
user = models.ForeignKey(User, on_delete=models.CASCADE)
message = models.TextField()
response = models.TextField()
timestamp = models.DateTimeField(auto_now_add=True)

text

---

## Note on User Model Implementation

*Assignment Context:*  
The original assignment provided a plain User model that did not extend Django’s built-in user system. However, in Django projects—especially when using authentication and JWT—it is necessary and best practice to use a custom user model inheriting from AbstractUser or AbstractBaseUser.

*Why this change?*

- Django’s authentication system, admin panel, and JWT authentication expect a Django auth user model.
- Using a plain model causes errors such as “User not found” during authentication because these systems look for the Django auth user table.
- This project uses a custom user model to ensure:
  - Full compatibility with Django’s authentication backends.
  - Seamless JWT token handling.
  - Ability to add extra fields like tokens for application-specific features.

*Summary:*  
Although the assignment suggested a plain User model, using AbstractUser is necessary for the authentication features to work properly, and it aligns with Django best practices.

---

## How To Run This Project

1. *Set up a virtual environment*  
    
    python -m venv venv
    source venv/Scripts/activate  # Windows
    # or
    source venv/bin/activate      # macOS/Linux
    

2. *Install dependencies*  
    
    pip install -r requirements.txt
    

3. *Apply migrations*  
    
    python manage.py makemigrations
    python manage.py migrate
    

4. *Start the development server*  
    
    python manage.py runserver
    

5. **Import Postman Collection**

    Import `AI_Chat_API.postman_collection.json` into Postman to test the APIs easily.

    [AI_Chat_API.postman_collection.json](https://github.com/SaurabhSB07/chat_api/blob/main/AI_Chat_API.postman_collection.json)

    **How to import into Postman:**
    1. Open Postman.
    2. Click on **Import**.
    3. Select the file `AI_Chat_API.postman_collection.json`.
    4. Use the pre-configured requests to test registration, login, chat, and token balance.
---

## API Endpoints

| Endpoint           | Method | Description                           |
|--------------------|--------|---------------------------------------|
| /api/register/     | POST   | Register a new user                   |
| /api/login/        | POST   | User login, obtain JWT tokens         | 
| /api/chat_msg/     | POST   | Send message to AI chat               |
| /api/tokenbalance/ | GET    | View remaining token balance          |
| /api/token/        | POST   | Obtain JWT access and refresh tokens  |
| /api/token/refresh/| POST   | Refresh JWT access token              |

---

## Usage Details

- Each registered user starts with *4000 tokens*.
- Each chat message costs *100 tokens*, which are deducted from user balance.
- AI responses are currently dummy placeholders that can be extended.
- JWT tokens are required for protected endpoints.
- Proper HTTP status codes and error handling ensure robustness.

---

## Demo and Explanation

This project is designed for demonstration during interviews, showcasing:

- Clear architecture using Django REST Framework.
- Secure JWT authentication and authorization.
- Token management integrated into user accounts.
- Storing and serving chat history.
- Easy API testing via Postman.

---

Thank you for considering my application. 