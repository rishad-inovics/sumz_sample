from django.db import models

# Create your models here.


class Questions(models.Model):
    text = models.CharField(max_length=250)
    option1 = models.CharField(max_length=120)
    option2 = models.CharField(max_length=120)
    option3 = models.CharField(max_length=120)
    option4 = models.CharField(max_length=120)
    correct_option = models.CharField(max_length=120)
    sheet = models.CharField(max_length=120)
    file_name = models.CharField(max_length=120, null=True)
