from django.urls import path
from . import views

urlpatterns = [
    path('budgets/<int:pky>/<int:pkm>', views.budget_resume, name='budgets'),
    path('graphs/<int:pky>/<int:pkm>', views.graphs_resume, name='graphs'),
]