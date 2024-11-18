from django.db import models
from datetime import date

class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    join_date = models.DateField(default=date.today)
    contribution = models.DecimalField(max_digits=10, decimal_places=2, default=35.00)

class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, choices=[(20, '20%'), (15, '15%'), (10, '10%')])
    repayment_period = models.PositiveIntegerField(choices=[(1, '1 Month'), (2, '2 Months'), (3, '3 Months')])
    start_date = models.DateField(default=date.today)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')

class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    payment_date = models.DateField(default=date.today)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_number = models.CharField(max_length=20)
