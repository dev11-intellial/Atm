from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class User_balance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=6,decimal_places=2)



class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit = models.DecimalField(max_digits=6,decimal_places=2)

class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    withdraw = models.DecimalField(max_digits=6,decimal_places=2)
