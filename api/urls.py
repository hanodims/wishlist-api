from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api-login"),
    path('register/', views.Register.as_view(), name="api-register"),

    path('', views.ItemList.as_view(), name="api-list"),
    path('<int:item_id>/', views.ItemDetail.as_view(), name="api-detail"),
]
