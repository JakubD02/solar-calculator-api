from django.urls import path

from .views import CalculateLayoutView, CalculationListView, CalculationDetailView, CalculationMountsView, CalculationJointsView

urlpatterns = [
    path("calculate/", CalculateLayoutView.as_view(), name="calculate-layout"),
    path("calculations/", CalculationListView.as_view(), name="calculation-history-list"),
    path("calculations/<int:pk>", CalculationDetailView.as_view(), name="calculation-history-detail"),
    path("calculations/<int:pk>/mounts/", CalculationMountsView.as_view(), name="calculation-mounts"),    
    path("calculations/<int:pk>/joints/", CalculationJointsView.as_view(), name="calculation-joints"),
]
