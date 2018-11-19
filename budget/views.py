from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.db.models import Avg, Count, Min, Sum
import calendar
from entry.methods import *
import datetime
# Create your views here.
def budget_resume(request,pky=datetime.datetime.now().year,pkm=datetime.datetime.now().month):
    today = datetime.datetime.now()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tables = []
    per = 0
    res = 0
    inc = 0
    tot = 0
    bar = 0
    budgets = []
    start_date = datetime.date(pky,pkm,1)
    r = calendar.monthrange(pky,pkm)
    days = range(1,r[1])
    end_date = datetime.date(pky,pkm,r[1])
    income = round(total_month_income(start_date, end_date),2)
    bud = Budget.objects.filter(date__month=start_date.month)
    for b in bud :
        values = Outcome.objects.filter(date__range=[start_date, end_date],category=b.category)
        outcome_total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
        p = round(float(b.amount)/income*100,2) if income != 0 else 0.00
        per += p
        r = round(b.amount-outcome_total,2)
        res += r
        i = round(outcome_total,2)
        inc += i
        t = round(float(b.amount),2)
        tot += t
        g = round(float(i)/float(b.amount),2)*100 if float(b.amount) !=0 else 0.00
        bar += g
        budgets.append([b, p, r, i ,g])
    
    budgets.append([{'category':'Total','amount':tot}, per,res,inc,round(float(inc)/float(tot),2)*100 if float(tot) !=0 else 0.00])
    tables.append([start_date,end_date,budgets,income]) 
    thismonth = start_date.month
    print(thismonth)
    return render(request, 'budgets.html', {'color':'blue', 'today':today,'thismonth':thismonth, 'tables':tables,'months':months})
