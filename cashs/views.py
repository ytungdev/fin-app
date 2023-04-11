from django.shortcuts import render, redirect
from .models import CashRecord
from accounts.models import Account
from datetime import date
import os
import csv


def records(request):
  records = CashRecord.objects.all().values()
  context = {
    'records': records,
  }
  return render(request, 'all_records.html', context)

def add_record(request):
  accounts = Account.objects.all().values()
  if request.method == 'POST':
    data = request.POST
    print(data)
    for ac in accounts:
      res = data.get(f"ac_{ac['id']}")
      d =  data.get("date") if data.get("date") else date.today()
      if res:
        ## new entry to db
        new_rec = CashRecord()
        new_rec.account_id = ac['id']
        new_rec.date = d
        new_rec.balance = res
        new_rec.save()
        print(f"{ac['id']} : {new_rec}")
      else:
        print(f"nope : {ac['id']}")
    return redirect('/dashboard')
  else:
    prev_bal = []
    for ac in accounts:
      bal = CashRecord.objects.filter(account=ac['id']).order_by('-date').values()
      if bal:
        prev_bal.append(bal[0]['balance'])
      else:
        prev_bal.append("")
    context = {
      'accounts': zip(accounts, prev_bal)
    }
    # print(prev_bal)
    return render(request, 'add_cash_record.html', context)
 
def load(request):
  f = os.path.join('statics', 'secret', "cashrecords.csv")
  with open(f, mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
      ac = Account.objects.filter(name=row[0].strip()).values()[0]
      if ac:
        a = ac["id"]
        d = row[1].strip()
        b = row[2].strip()
        rec = CashRecord.objects.filter(account=a, date=d).values()
        if rec:
          print(f'record exist : {d} - {ac["name"]}')
        else:
          new_rec = CashRecord()
          new_rec.account_id = a
          new_rec.date = d
          new_rec.balance = b
          new_rec.save()
      else:
        print(f"account not exist : {row[0]}")
  return redirect('/dashboard')

