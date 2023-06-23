from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import CurrencyRecord
from accounts.models import Account
import utils

from datetime import date, datetime
import requests


def records(request):
    records = CurrencyRecord.objects.all().values()
    context = {
        'records': records,
    }
    return render(request, 'all_records.html', context)


def add_record(request):
    currs = Account.objects.order_by().values_list('curr', flat=True).distinct()
    # recieve form
    if request.method == 'POST':
        data = request.POST
        # print(data)
        for curr in currs:
            res = data.get(f"rate_{curr}")
            d = data.get("date") if data.get("date") else date.today()
            if res:
                # new entry to db
                new_rec = CurrencyRecord()
                new_rec.curr = curr
                new_rec.date = d
                new_rec.rate = res
                new_rec.save()
                print(f"{curr} : {new_rec}")
            else:
                print(f"nope : {curr}")
        return redirect('/dashboard')
    # render form
    else:
        prev_rate = []
        for curr in currs:
            bal = CurrencyRecord.objects.filter(
                curr=curr).order_by('-date').values()
            if bal:
                prev_rate.append(bal[0]['rate'])
            else:
                prev_rate.append("")
        context = {
            'currs': zip(currs, prev_rate),
            'date':date.today().strftime('%Y-%m-%d')
        }
        # print(zip(currs, prev_rate))
        return render(request, 'add_curr_record.html', context)


def fetch_curr(request):
    if request.method == "POST":
        data = request.POST
        d = data.get("date") if data.get("date") else date.today()
        currs = list(Account.objects.order_by().values_list(
            'curr', flat=True).distinct())
        rates = {}
        syms = ",".join(currs)
        print('Fetching ...')
        req = get_forex_api(d, syms)
        print(req)
        if req[0] != 200:
            return JsonResponse({"data": req[1]}, status=req[0])
        else:
            for curr in currs:
                rates[curr] = round(1 / req[1]["rates"][curr], 4)
            data = {
                "date": d,
                "currs": currs,
                "rates": rates
            }
            return JsonResponse({"data": data}, status=200)

def get_forex_api(d, syms):
    key = utils.use_env("FOREX_API_KEY")
    base = "HKD"
    url = f"https://api.apilayer.com/exchangerates_data/{d}?base={base}&symbols={syms}"
    payload = {}
    headers = {"apikey": key}
    response = requests.request("GET", url, headers=headers, data=payload)
    status_code = response.status_code
    result = response.json()
    return status_code, result
