from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView

# 🔥 Home page (API menu)
def home(request):
    return HttpResponse("""
        <h1>Django REST API 🚀</h1>

        <h3>Available APIs:</h3>

        <p>👉 <a href='/api/register/'>Register User</a></p>
        <p>👉 <a href='/api/token/'>Login (Get Token)</a></p>
        <p>👉 <a href='/api/items/'>Items API (Protected)</a></p>

        <hr>

        <h4>Steps:</h4>
        <ol>
            <li>Register user</li>
            <li>Login to get token</li>
            <li>Use token to access items</li>
        </ol>
    """)

urlpatterns = [
    path('', home),  # 👈 THIS FIXES YOUR REQUIREMENT

    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/', include('api.urls')),
]