from django.urls import path

from .views import InitView, DonationView, test_login_view

urlpatterns = [
    path('init/', InitView.as_view()),
    path('donation.register/', DonationView.as_view()),
    path('home/', test_login_view),
]
