from django.db import models
from django.contrib.auth.models import User

class StudentsProfile(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    mobile = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.username