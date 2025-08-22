# Social Media API

This project implements the foundational elements of a Social Media API using Django and Django REST Framework.  
It includes a custom user model, token-based authentication, and endpoints for registration, login, and profile management.

---

# Setup Process
The custom User model extends Django’s AbstractUser and includes:
bio – short text about the user
profile_picture – uploaded profile image
followers – Many-to-Many relationship (non-symmetrical) to allow following other users

# Authentication Flow
This API uses Token Authentication provided by Django REST Framework.
Register a User
Endpoint: POST /api/accounts/register/
