from rest_framework import serializers
from .models import OrderHistory, BinanceSymbol

class TradingBotSerializer(serializers.Serializer):
    wallet_address = serializers.CharField(max_length=200)
    secret_address = serializers.CharField(max_length=200)
    symbol = serializers.CharField(max_length=200)
    time_period = serializers.CharField(max_length=200)
    stop_profit = serializers.FloatField()
    stop_loss = serializers.FloatField()
    quantity = serializers.FloatField()


class StopTradingBotSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=200)

class StartTradingBotSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=200)

class OrderHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderHistory
        fields = "__all__"


#
# class SymbolSerialzier(serializers.ModelSerializer):
#
#     class Meta:
#         model = BinanceSymbol
#         fields = ('name', )
