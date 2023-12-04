from django.db import models

class Bag(models.Model):
    # Define fields for the Bag model
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    material = models.CharField(max_length=50)
    size = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.PositiveIntegerField(default=0)

    # Add any other fields as needed for your specific use case

    def __str__(self):
        return self.name
