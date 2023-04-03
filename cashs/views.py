from django.shortcuts import render
from .models import CashRecord
from accounts.models import Account

def records(request):
  records = CashRecord.objects.all().values()
  context = {
    'records': records,
  }
  return render(request, 'all_records.html', context)

def add_record(request):
  accounts = Account.objects.all().values()
  context = {
    'accounts': accounts,
  }
  return render(request, 'add_record.html', context)
