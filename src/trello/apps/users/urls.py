from django.urls import path

from .views import OTPView

urlpatterns = [
    path('/otp', OTPView.as_view(), name='otp_view')
]