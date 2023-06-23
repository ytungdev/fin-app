from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from .models import Account
from .forms import AccountForm
import os
import csv

class AccountList(generic.ListView):
  template_name = 'account_list.html'
  context_object_name = 'all_account'
  def get_queryset(self):
    return Account.objects.all()

def details(request, ac_id):
   ac = get_object_or_404(Account, pk=ac_id)
   if request.method == 'POST':
    ## receive new data and update db
    form = AccountForm(request.POST)
    if form.is_valid():
        ac.location = form.cleaned_data['location']
        ac.provider = form.cleaned_data['provider']
        ac.name = form.cleaned_data['name']
        ac.curr = form.cleaned_data['curr']
        ac.remark = form.cleaned_data['remark']
        ac.save()
        return HttpResponseRedirect('/accounts')
    else:
        print('invalid')
   else:
    ## display data
    form = AccountForm()
    form.fields["name"].initial = ac.name
    form.fields["location"].initial = ac.location
    form.fields["provider"].initial = ac.provider
    form.fields["curr"].initial = ac.curr
    form.fields["remark"].initial = ac.remark

    template = loader.get_template('account_details.html')
    context = {'form':form, 'data':ac}
    return HttpResponse(template.render(context, request))

def add_account(request):
  if request.method == 'POST':
    form = AccountForm(request.POST)
    if form.is_valid():
        new_ac = Account()
        new_ac.location = form.cleaned_data['location']
        new_ac.provider = form.cleaned_data['provider']
        new_ac.name = form.cleaned_data['name']
        new_ac.curr = form.cleaned_data['curr']
        new_ac.remark = form.cleaned_data['remark']
        new_ac.save()
        return HttpResponseRedirect('/accounts')
    else:
        print('invalid')
  else:
    form = AccountForm()
    #template = loader.get_template('add_account.html')
    template = loader.get_template('account_details.html')
    context = {'form':form, 'data':None}
    return HttpResponse(template.render(context, request))


def load(request):
  f = os.path.join('static', 'demo', "accounts.csv")
  with open(f, mode='r') as infile:
    reader = csv.reader(infile)
    for row in reader:
      l = row[0].strip()
      n = row[1].strip()
      p = row[2].strip()
      c = row[3].strip()
      r = row[4].strip()
      ac = Account.objects.filter(name=n).values()
      if ac:
        print(f'account exist : {n}')
      else:
        new_ac = Account()
        new_ac.location = l
        new_ac.provider = p
        new_ac.name = n
        new_ac.curr = c
        new_ac.remark = r
        new_ac.save()
    return redirect('/dashboard')

