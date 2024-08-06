from django.db import models


# Create your models here.

class OrderHistory(models.Model):
    order_symbol = models.CharField(max_length=100)
    order_side = models.CharField(max_length=50)
    order_price = models.FloatField()
    order_qty = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_symbol


class ProfitRatio(models.Model):
    profit_loss = models.FloatField()

    def __str__(self):
        return self.profit_loss


class BinanceSymbol(models.Model):
    name = models.CharField(max_length=100)
    tokenA = models.CharField(max_length=200)
    tokenB = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BinanceTimeFrame(models.Model):
    time_period = models.CharField(max_length=10)

    def __str__(self):
        return self.time_period
