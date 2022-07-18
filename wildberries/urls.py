from django import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
     path('', views.index, name='index'),
     path('<int:id>/', views.detail_product, name='detail_product'),
     path('accounts/', include('django.contrib.auth.urls')),
     path('signup/', views.RegisterUser.as_view(), name="signup"),
     path('favorite/<int:id>', views.favorite_product, name='favorite_product'),
     path('favorite_list/', views.favorite_list, name='favorite_list'),
     path('api/v1/productslist/', views.PoductsAPIView.as_view()),
]
