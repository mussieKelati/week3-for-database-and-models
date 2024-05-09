from django.db import models
class student (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    def __str__(self):
        return f"{self.first_name},{self.last_name} is {self.age} old"
    