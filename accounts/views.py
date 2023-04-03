from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views import generic
from django.shortcuts import get_object_or_404
from .models import Account
from .forms import AccountForm

class AccountList(generic.ListView):
  template_name = 'account_list.html'
  context_object_name = 'all_account'
  def get_queryset(self):
    return Account.objects.all()

def details(request, ac_id):
   ac = get_object_or_404(Account, pk=ac_id)
   if request.method == 'POST':
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


def testing(request):
  data = Account.objects.filter(provider='HSBC', location="HK").values()
  template = loader.get_template('testing.html')
  context = {
    'data': data,
  }
  return HttpResponse(template.render(context, request))
