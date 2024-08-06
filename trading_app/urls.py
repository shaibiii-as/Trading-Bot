from django.urls import path, include
from trading_app import views
from .models import OrderHistory
from .serializers import OrderHistorySerializer

urlpatterns = [
    path('create_trading_bot/', views.CreateTradingBotAPIView.as_view(), name="create-trading-data"),
    path('test/', views.TestView.as_view(), name="test"),
    path('start_trading_bot/', views.StartTradingBotAPIView.as_view(), name="start-trading-bot"),
    path('stop_trading_bot/', views.StopTradingBotAPIView.as_view(), name="stop-trading-bot"),
    path('orders_history/', views.OrderHistoryAPIView.as_view(queryset=OrderHistory.objects.all(),
                                                              serializer_class=OrderHistorySerializer),
         name='history-list'),
]

