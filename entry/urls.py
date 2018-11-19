from django.urls import path
from . import views

urlpatterns = [
    path('<int:pky>/<int:pkm>', views.accounts_resume, name='resume'),
    path('', views.accounts_resume, name='resume'),
    path('outcomes/<int:pky>/<int:pkm>', views.outcomes_resume, name='outcome'),
    path('outcomes', views.outcomes_resume, name='outcome'),
    path('incomes', views.incomes_resume, name='income'),
    path('transfers', views.transfers_resume, name='transfer'),
    path('outcome-add', views.outcome_add, name='outcome-add'),
    path('income-add', views.income_add, name='income-add'),
]