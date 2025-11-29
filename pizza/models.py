from django.db import models

class Order(models.Model):
    PIZZA_TYPE_CHOICES = [
        ('veg', 'Veg'),
        ('nonveg', 'Non-Veg'),
    ]

    pizza_name = models.CharField(max_length=100)
    pizza_type = models.CharField(max_length=10, choices=PIZZA_TYPE_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.pizza_name} ({self.pizza_type}) x{self.quantity}"

