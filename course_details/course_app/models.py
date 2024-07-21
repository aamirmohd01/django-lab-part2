from django.db import models

# Create your models here.
class Subjects(models.Model):
    sub_code = models.CharField(max_length=20)
    sub_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sub_name
