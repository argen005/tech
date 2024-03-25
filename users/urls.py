from django.urls import path
from users.views import RegisterAPIView, LoginAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # path('send_url_email/', EmailSendURLView.as_view(), name='send_url_email'),
    # path('email_verify/', EmailVerifyView.as_view(), name='email_verify'),
]