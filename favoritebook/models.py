from django.db import models
from loginapp.models import User
import datetime
import re


class BookManager(models.Manager):
#     def registration_validator(self, postData):
#         errors = {}
#         if len(postData['first_name']) < 2:
#             errors["first_name"] = "First Name must be at least 2 characters"
#         if len(postData['last_name']) < 2:
#             errors["last_name"] = "Last Name must be at least 3 characters"
#         EMAIL_REGEX = re.compile(
#             r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):
#             errors['email'] = "Invalid email address!"
#         users = User.objects.all()
#         emaillist = []
#         for user in users:
#             emaillist.append(user.email)
#         if postData['email'] in emaillist:
#             errors['duplicate'] = "That email already exists"
#         if (datetime.date.today() < datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d").date()):
#             errors['date'] = "Birthday must be in the past"
#         if (len(postData['password']) < 8):
#             errors['password'] = "Password must be at least 8 characters"
#         if postData["password2"] != postData["password"]:
#             errors["passwordmatch"] = "Your passwords do not match!"
#         return errors
    
    def book_validator(self, postData):
        book_errors = {}
        if (len(postData['title']) < 1):
            book_errors['title'] = "Books must have a title."
        if (len(postData['desc']) < 5):
            book_errors['desc'] = "Description must be at least 5 characters.  Make em count!"
        return book_errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by_id = models.ForeignKey(User, related_name="uploads", on_delete = models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name='favorite_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

