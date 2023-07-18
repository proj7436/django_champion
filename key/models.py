from django.db import models

# Create your models here.


class Key(models.Model):
    key = models.CharField(max_length=255)
    class_key = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.class_key
    

class SourceCode(models.Model):
    code = models.TextField()
    key_update = models.CharField(max_length=100)