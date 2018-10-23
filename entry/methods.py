from .models import *
from django.db.models import Avg, Count, Min, Sum
from django.db.models.functions import Coalesce
import re
from datetime import timedelta

def i_date(date, account):
        income = Income.objects.filter(date__lt=date,account=account).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        return income    

def o_date(date, account):
        outcome = Outcome.objects.filter(date__lt=date,account=account).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        return outcome     

def t_date(date, account):
        transfer_to = Transfer.objects.filter(date__lt=date,to_account=account).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        transfer_from = Transfer.objects.filter(date__lt=date,from_account=account).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        return transfer_to-transfer_from

def balance_date(date, account):
        i = i_date(date,account)
        o = o_date(date,account)
        t = t_date(date,account)
        return i-o+t

def total_month_income(start_date, end_date):
        income = Income.objects.filter(date__range=[start_date, end_date]).aggregate(total=Coalesce(Sum('amount'), 0))['total'] 
        return float(income) if income is not None else 0.00

def month_income(start_date, end_date, account):
        income = Income.objects.filter(date__range=[start_date, end_date],account=account.id).aggregate(total=Coalesce(Sum('amount'), 0))['total'] 
        return float(income) if income is not None else 0.00

def month_outcome(start_date, end_date, account):
        outcome = Outcome.objects.filter(date__range=[start_date, end_date],account=account.id).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        return float(outcome) if outcome is not None else 0.00

def month_transfer(start_date, end_date, account):
        transfer_to = Transfer.objects.filter(date__range=[start_date, end_date],to_account=account.id).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        transfer_from = Transfer.objects.filter(date__range=[start_date, end_date],from_account=account.id).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        return float(transfer_to-transfer_from if transfer_from is not None and transfer_to is not None else 0.00)

def outcome_of_category_in_month(start_date,end_date,category,deep):
        total = Outcome.objects.filter(date__range=[start_date, end_date],category=category).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        sons = Category.objects.filter(father=category)
        if deep:
                for son in sons:
                        total += Outcome.objects.filter(date__range=[start_date, end_date],category=son).aggregate(total=Coalesce(Sum('amount'), 0))['total']
        return round(float(total),2) if total is not None else 0.00

def category_graph(start_date,end_date,total):
        category_fathers = Category.objects.filter(father=None)
        results = []
        if total!= 0:
                for category in category_fathers:
                        father_alone = outcome_of_category_in_month(start_date,end_date,category,False)
                        father_total = outcome_of_category_in_month(start_date,end_date,category,True)
                        categories = Category.objects.filter(father=category)
                        categories_names = []
                        sons_totals = []
                        for categori in categories:
                                son_total = outcome_of_category_in_month(start_date,end_date,categori,False)
                                sons_totals.append(str(round(son_total/float(total)*100,2)).replace(",","."))
                                categories_names.append(str(categori.name))
                        if not categories:
                                sons_totals.append(str(round(father_total/float(total)*100,2)).replace(",","."))
                                categories_names.append(str(category.name))
                        else:
                                sons_totals.append(str(round(father_alone/float(total)*100,2)).replace(",","."))
                                categories_names.append(str(category.name))
                        results.append([str(round(father_total/float(total)*100,2)).replace(",","."),category.name,categories_names,sons_totals])
        return results

def timeline_graph(start_date,r,income):
        total = []
        proyected = []
        daily = []
        pd =[]
        for i in range(0,r):
                outcome = Outcome.objects.filter(date=start_date+datetime.timedelta(days=i)).aggregate(total=Coalesce(Sum('amount'), 0))['total']
                value = round(float(outcome),2) if outcome is not None else 0.00
                summatory = value + round(float(total[i-1]),2) if i != 0 else value 
                total += [str(summatory).replace(",",".")]
                pd += [str((income)/r).replace(",",".")]
                proyected += [str((income)/r*i).replace(",",".")]
                daily += [str(value).replace(",",".")]
        return [["Outcome",total],["Proyected monthly",proyected],["Daily",daily],["Proyected monthly",pd]]