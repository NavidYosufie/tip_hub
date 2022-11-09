from django.db import models

class Profile(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    about_you = models.TextField()

    def __str__(self):
        return f"{self.fname}  -   {self.about_you}"


