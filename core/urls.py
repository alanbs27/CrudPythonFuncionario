from django.contrib import admin
from django.urls import path
from funcionario import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp/', views.emp, name='emp'),
    path('', views.show),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
