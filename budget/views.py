from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.db.models import Avg, Count, Min, Sum
import calendar
from entry.methods import *
import datetime
# Create your views here.
def budget_resume(request):
    today = datetime.datetime.now()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tables = []
    for i in range(1,13) :
        start_date = datetime.date(today.year,i,1)
        r = calendar.monthrange(today.year,i)
        days = range(1,r[1])
        end_date = datetime.date(today.year,i,r[1])
        budgets = Budget.objects.filter(date__month=start_date.month)
        income = round(total_month_income(start_date, end_date),2)
        tables.append([start_date,end_date,budgets,income]) 
    return render(request, 'budgets.html', {'today':today, 'tables':tables,'months':months})
