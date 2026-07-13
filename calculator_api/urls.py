from django.urls import path

from .views import CalculateLayoutView, CalculationHistoryListView

urlpatterns = [
    path("calculate/", CalculateLayoutView.as_view(), name="calculate-layout"),
    path("calculations/", CalculationHistoryListView.as_view(), name="calculation-history-list"),
]
