from django.urls import path
from task_manager import views

urlpatterns = [
    path('', views.FirstApiView.as_view(), name='firstApi')
]