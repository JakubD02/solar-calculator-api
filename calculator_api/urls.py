from django.urls import path

from .views import CalculateLayoutView

urlpatterns = [
    path("calculate/", CalculateLayoutView.as_view(), name="calculate-layout"),
]
