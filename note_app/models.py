from django.db import models
# Create your models here.

class notetypeyes(models.Model):

    Heading=models.TextField(max_length=20)
    Content=models.TextField(max_length=100)
    Lastupdated=models.DateTimeField(auto_now_add=True)
    
    """
    Heading="roja"
    Content="testing"
    Lastupdated="dgn"
    """