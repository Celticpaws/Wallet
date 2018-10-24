from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.db.models import Avg, Count, Min, Sum
import calendar
from .methods import *
import datetime
# Create your views here.

def accounts_resume(request):
    accounts = Account.objects.all()
    today = datetime.datetime.now()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tables = []
    for i in range(1,12) :
        starts = []
        values = [[],[],[],[],[],[]]
        outcomes = []
        transfers = []
        start_date = datetime.date(today.year,i,1)
        r = calendar.monthrange(today.year,i)
        end_date = datetime.date(today.year,i,r[1])
        for account in accounts :
            values[0].append(round(balance_date(start_date,account),2))
            values[1].append(round(month_income(start_date, end_date, account),2))
            values[2].append(round(month_outcome(start_date, end_date, account),2))
            values[3].append(round(month_transfer(start_date, end_date, account),2))
        values[4]= [round(float(a) -float(b) + float(c),2) for a,b,c in zip(values[1], values[2], values[3])]
        values[5]= [round(float(a) +float(b),2) for a,b in zip(values[4], values[0])]
        total = sum(values[5])
        incomes = sum(values[1])
        outcomes = sum(values[2])
        print(outcomes)
        inc = incomes/(incomes+outcomes) if incomes+outcomes >0 else 0
        ouc = outcomes/(incomes+outcomes) if incomes+outcomes >0 else 0
        values = [a+b for a,b in zip([['Start'],['Income'],['Outcome'],['Transfer'],['SubTotal'],['Total']],values)]

        tables.append([start_date,end_date,values,round(total,2),inc*100,ouc*100])
        
    return render(request, 'resume.html', {'today':today, 'accounts': accounts, 'tables':tables,'months':months})

def outcomes_resume(request):
    today = datetime.datetime.now()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tables = []
    for i in range(1,13) :
        start_date = datetime.date(today.year,i,1)
        r = calendar.monthrange(today.year,i)
        days = range(1,r[1])
        end_date = datetime.date(today.year,i,r[1])
        values = Outcome.objects.filter(date__range=[start_date, end_date])
        total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
        categories = Category.objects.filter(father=None)
        circle = category_graph(start_date,end_date,total)
        incomes = total_month_income(start_date,end_date)
        line = timeline_graph(start_date,r[1],incomes)
        thismonth = today.month
        tables.append([start_date,end_date,values,round(total,2),circle,line]) 
    return render(request, 'outcomes.html', {'today':today, 'thismonth':thismonth, 'tables':tables,'months':months,'categories':categories,'days':days})

def outcome_add(request):
    return render(request, 'add-outcome.html', {})

def incomes_resume(request):
    today = datetime.datetime.now()
    start_date = datetime.date(today.year,1,1)
    end_date = datetime.date(today.year,12,31)
    values = Income.objects.filter(date__range=[start_date, end_date])
    total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
    tables = [start_date,end_date,values,round(total,2)] 
    return render(request, 'incomes.html', {'today':today, 'tables':tables})

def transfers_resume(request):
    today = datetime.datetime.now()
    start_date = datetime.date(today.year,1,1)
    end_date = datetime.date(today.year,12,31)
    values = Transfer.objects.filter(date__range=[start_date, end_date])
    total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
    tables = [start_date,end_date,values,round(total,2)] 
    return render(request, 'transfer.html', {'today':today, 'tables':tables})