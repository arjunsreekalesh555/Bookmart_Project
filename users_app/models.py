from django.contrib.auth.models import User
from django.db import models
from rsbooks_app.models import RSBook

# Create your models here.
class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    items=models.ManyToManyField(RSBook)

class cartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    book=models.ForeignKey(RSBook, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)