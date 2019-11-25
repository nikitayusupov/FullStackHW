
from django.db import models
from django.contrib.auth.models import User


class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=False)
    message = models.CharField(max_length=500, blank=True)        
    # null=True так как у нас уже были какие то данные в таблице и мы хотим чтобы ничего не сломалось когда мы добавляем новое поле
    owner = models.ForeignKey(
        User, related_name="leads", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# CASCADE: 
# When the referenced object is deleted,
#  also delete the objects that have references to it 
