from django.db import models

# Create your models here.
class ToDo(models.Model):
    tid = models.AutoField(primary_key=True)
    desc = models.TextField()


    # python manage.py makemigrations
    # python manage.py migrate