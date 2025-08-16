from django.db import models

# Create your models here.
class Transaction(models.Model):
    account = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    
    CATEGORY_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense')
    ]

    category = models.CharField(max_length=7, choices=CATEGORY_CHOICES)

    description = models.CharField(max_length=255, blank=True)  