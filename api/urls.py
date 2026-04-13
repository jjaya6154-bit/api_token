from django.urls import path
from .views import ItemListCreateView, RegisterView, api_dashboard

urlpatterns = [
    path('', api_dashboard),              # 👈 Dashboard (root API)
    path('items/', ItemListCreateView.as_view()),  # GET + POST items
    path('register/', RegisterView.as_view()),     # Register user
]