from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return f"{self.name} : {self.price}"

class TableBooking(models.Model):
    customer_name = models.CharField(max_length=100)
    booking_date = models.DateTimeField()
    number_of_guests = models.IntegerField()
    def __str__(self):
        return f"{self.customer_name} - {self.booking_date}"
