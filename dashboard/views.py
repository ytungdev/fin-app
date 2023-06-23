from django.shortcuts import render, redirect
from django.http import JsonResponse

from accounts.models import Account
from cashs.models import CashRecord
from currencies.models import CurrencyRecord

from datetime import date
import calendar
import csv
import json
import os



def main(request):
    context = {}
    return render(request, 'main.html', context)


def monthly_cash(request, yr=date.today().year, mo=date.today().month):
    accounts = Account.objects.all().values()
    rec_cash = []
    rec_rate = []
    vals = []
    d = date_range(yr, mo)
    for ac in accounts:
        bal = CashRecord.objects.filter(account=ac['id']).filter(
            date__range=(d[0], d[1])).order_by('-date').values()
        if bal:
            bal = bal[0]['balance']
        else:
            bal = 0

        rate = CurrencyRecord.objects.filter(curr=ac['curr']).filter(
            date__range=(d[0], d[1])).order_by('-date').values()
        if rate:
            rate = rate[0]['rate']
        else:
            rate = 1

        rec_cash.append(bal)
        rec_rate.append(rate)
        vals.append(bal * rate)
    data = zip(accounts, rec_cash, rec_rate, vals)
    context = {
        'yr': yr,
        'mo': mo,
        'data': data,
        'sum': sum(vals)
    }
    return render(request, 'monthly_cash.html', context)


def date_range(yr, mo):
    # return first and last date.obj from yr, mo
    last_d = calendar.monthrange(yr, mo)[1]
    return date(yr, mo, 1), date(yr, mo, last_d)


def get_utils(request):
    return render(request, 'utils.html')


def testing(request):
    return JsonResponse({'result':[]})
