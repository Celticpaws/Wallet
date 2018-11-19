from django.urls import path
from . import views

urlpatterns = [
    path('budgets/<int:pky>/<int:pkm>', views.budget_resume, name='budgets'),
]