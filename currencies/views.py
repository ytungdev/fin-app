from django.shortcuts import render, redirect
from .models import CurrencyRecord
from accounts.models import Account
from datetime import date

def records(request):
  records = CurrencyRecord.objects.all().values()
  context = {
    'records': records,
  }
  return render(request, 'all_records.html', context)

def add_record(request):
  currs = Account.objects.order_by().values_list('curr', flat=True).distinct()
#   print(currs)
  if request.method == 'POST':
    data = request.POST
    # print(data)
    for curr in currs:
      res = data.get(f"rate_{curr}")
      d =  data.get("date") if data.get("date") else date.today()
      if res:
        ## new entry to db
        new_rec = CurrencyRecord()
        new_rec.curr = curr
        new_rec.date = d
        new_rec.rate = res
        new_rec.save()
        print(f"{curr} : {new_rec}")
      else:
        print(f"nope : {curr}")
    return redirect('/dashboard')
  else:
    prev_rate = []
    for curr in currs:
      bal = CurrencyRecord.objects.filter(curr=curr).order_by('-date').values()
      if bal:
        prev_rate.append(bal[0]['rate'])
      else:
        prev_rate.append("")
    context = {
      'currs': zip(currs, prev_rate)
    }
    # print(zip(currs, prev_rate))
    return render(request, 'add_curr_record.html', context)
