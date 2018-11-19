from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.db.models import Avg, Count, Min, Sum
import calendar
from .methods import *
import datetime
from .forms import *
# Create your views here.

def accounts_resume(request,pky=datetime.datetime.now().year,pkm=datetime.datetime.now().month):
    accounts = Account.objects.all()
    today = datetime.datetime.now()
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tables = []
    starts = []
    values = [[],[],[],[],[],[]]
    outcomes = []
    transfers = []
    start_date = datetime.date(pky,pkm,1)
    r = calendar.monthrange(pky,pkm)
    end_date = datetime.date(pky,pkm,r[1])
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
    thismonth = start_date.month
    inc = incomes/(incomes+outcomes) if incomes+outcomes >0 else 0
    ouc = outcomes/(incomes+outcomes) if incomes+outcomes >0 else 0
    values = [a+b for a,b in zip([['Start'],['Income'],['Outcome'],['Transfer'],['SubTotal'],['Total']],values)]

    tables.append([start_date,end_date,values,round(total,2),inc*100,ouc*100])
        
    return render(request, 'resume.html', {'color': 'blue', 'today':today, 'thismonth':thismonth, 'accounts': accounts, 'tables':tables,'months':months,})

def outcomes_resume(request,pky=datetime.datetime.now().year,pkm=datetime.datetime.now().month):
    today = datetime.date(pky,pkm,1)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    tables = []
    start_date = datetime.date(today.year,today.month,1)
    r = calendar.monthrange(today.year,today.month)
    days = range(1,r[1])
    end_date = datetime.date(today.year,today.month,r[1])
    values = Outcome.objects.filter(date__range=[start_date, end_date])
    total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
    categories = Category.objects.filter(father=None)
    circle = category_graph(start_date,end_date,total)
    incomes = total_month_income(start_date,end_date)
    line = timeline_graph(start_date,r[1],incomes)
    thismonth = today.month
    tables.append([start_date,end_date,values,round(total,2),circle,line]) 
    return render(request, 'outcomes.html', {'color': 'red','today':today, 'thismonth':thismonth, 'tables':tables,'months':months,'categories':categories,'days':days})

def income_add(request):
    if request.method =="POST":
        form = IncomeForm(request.POST)
        form.is_valid()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('income')
        else:
            print(form)
            print(form.errors.as_data())
    else:
        form = IncomeForm()
        print(form.fields)
        categories = Category.objects.all()
        accounts = Account.objects.all()
    return render(request, 'add-income.html', {'form':form,'color': 'teal','categories':categories,'accounts':accounts})

def outcome_add(request):
    if request.method =="POST":
        form = OutcomeForm(request.POST)
        form.is_valid()
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('outcome',pky=datetime.datetime.now().year,pkm=datetime.datetime.now().month)
        else:
            print(form)
            print(form.errors.as_data())
    else:
        form = OutcomeForm()
        print(form.fields)
        categories = Category.objects.all()
        accounts = Account.objects.all()
    return render(request, 'add-outcome.html', {'form':form,'color': 'red','categories':categories,'accounts':accounts})

def incomes_resume(request):
    today = datetime.datetime.now()
    start_date = datetime.date(today.year,1,1)
    end_date = datetime.date(today.year,12,31)
    values = Income.objects.filter(date__range=[start_date, end_date])
    total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
    tables = [start_date,end_date,values,round(total,2)] 
    return render(request, 'incomes.html', {'color': 'teal', 'today':today, 'tables':tables})

def transfers_resume(request):
    today = datetime.datetime.now()
    start_date = datetime.date(today.year,1,1)
    end_date = datetime.date(today.year,12,31)
    values = Transfer.objects.filter(date__range=[start_date, end_date])
    total = values.aggregate(total=Coalesce(Sum('amount'), 0))['total']
    tables = [start_date,end_date,values,round(total,2)] 
    return render(request, 'transfer.html', {'color': 'purple', 'today':today, 'tables':tables})