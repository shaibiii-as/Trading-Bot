from django.contrib import admin
from .models import BinanceSymbol, BinanceTimeFrame, OrderHistory, ProfitRatio

# Register your models here.
admin.site.register(BinanceSymbol)
admin.site.register(BinanceTimeFrame)
admin.site.register(OrderHistory)
admin.site.register(ProfitRatio)