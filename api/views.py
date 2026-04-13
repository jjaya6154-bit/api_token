from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Item
from .serializers import ItemSerializer, RegisterSerializer

# 🔹 Register API
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


# 🔹 Items API (GET + POST)
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.AllowAny]  # use IsAuthenticated later


# 🔹 Dashboard API (ALL IN ONE)
@api_view(['GET'])
def api_dashboard(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response({
        "message": "Django REST API Dashboard 🚀",

        "endpoints": {
            "register": "/api/register/",
            "login": "/api/token/",
            "items": "/api/items/"
        },

        "items_data": serializer.data
    })