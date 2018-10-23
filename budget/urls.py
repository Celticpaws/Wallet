from django.urls import path
from . import views

urlpatterns = [
    path('budgets',views.budget_resume, name='budgets')
]