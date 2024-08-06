import os
import threading
import time
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from django.views import View
from rest_framework.response import Response
from trading_app.trading_bot_coins.ema_strategy import TradingBot
from threading import Thread
from .models import ProfitRatio, OrderHistory, BinanceSymbol, BinanceTimeFrame
from .serializers import TradingBotSerializer, OrderHistorySerializer, StartTradingBotSerializer, \
    StopTradingBotSerializer
import asyncio

# Create your views here.

trading_bot_dict = dict()


class CreateTradingBotAPIView(APIView):
    """
    TradingBotDetailAPIView class

    This view performs POST operation for get the users data

    Parameters
    ----------
    APIView : rest_framework.views

    """

    serializer_class = TradingBotSerializer
    fields = "__all__"

    @swagger_auto_schema(
        request_body=TradingBotSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request, *args, **kwargs):
        serialized = TradingBotSerializer(data=request.data)
        if serialized.is_valid():
            wallet_address = request.data['wallet_address']
            secret_key = request.data['secret_address']
            symbol_obj = BinanceSymbol.objects.get(name=request.data['symbol'].upper())
            time_frame = request.data['time_period']
            stop_profit = float(request.data['stop_profit'])
            stop_loss = float(request.data['stop_loss'])
            quantity = float(request.data['quantity'])
            trading_bot = TradingBot(wallet_address=wallet_address, wallet_secret_key=secret_key,
                                     tokenA=symbol_obj.tokenA,
                                     tokenB=symbol_obj.tokenB, symbol=symbol_obj.name, time_period=time_frame,
                                     stop_profit=stop_profit,
                                     stop_loss=stop_loss, quantity=quantity
                                     )
            trading_bot_dict[symbol_obj.name] = trading_bot
            message = "Your Trading Bot is created successfully"
            return Response(message)


class StartTradingBotAPIView(APIView):

    @swagger_auto_schema(
        request_body=StartTradingBotSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        serializer = StartTradingBotSerializer(data=request.data)
        if serializer.is_valid():
            symbol = request.data['symbol']
            for key, value in trading_bot_dict.items():
                if key == symbol:
                    trading_bot_dict[key].start_process()
                    break
            message = "Your Trading Bot is In-Progress"
            return Response(message)


class StopTradingBotAPIView(APIView):

    @swagger_auto_schema(
        request_body=StopTradingBotSerializer,

        responses={
            200: "OK",
            400: "Bad Request",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        serializer = StartTradingBotSerializer(data=request.data)
        if serializer.is_valid():
            symbol = request.data['symbol']
            for key, value in trading_bot_dict.items():
                if key == symbol:
                    trading_bot_dict[key].kill_process()
                    del trading_bot_dict[key]
                    break
            message = "Your Trading Bot is Stop"
            return Response(message)


class OrderHistoryAPIView(ListAPIView):
    """
    OrderHistoryAPIView class

    This view show the history data of trading bot

    Parametersg
    ----------
    APIView : rest_framework.views

    """
    queryset = OrderHistory.objects.all()
    serializer_class = OrderHistorySerializer

    @staticmethod
    async def wait_time(await_time):
        await asyncio.sleep(await_time)
        return

    def list(self, request):
        queryset = self.get_queryset()
        serializer = OrderHistorySerializer(queryset, many=True)
        asyncio.run(self.wait_time(10))
        return Response(serializer.data)


class StopTradingBotView(View):

    def post(self, request):
        pass


class TestView(View):

    def get(self, request):
        return render(request, 'test.html')

