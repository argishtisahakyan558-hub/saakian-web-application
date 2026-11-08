from django.db import models


class Order(models.Model):
    customer_name = models.CharField(max_length=150)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    delivery_address = models.TextField()

    def __str__(self):
        return f"Заказ №{self.pk} — {self.customer_name}"