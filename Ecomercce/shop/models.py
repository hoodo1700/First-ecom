from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,)
    
    def __str__(self):
        return self.name
class poromotion(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):
        return f"{self.user.username}'s cart"
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.cart.user.username}'s cart item"
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    

    
