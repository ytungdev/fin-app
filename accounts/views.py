from django.http import HttpResponse
from django.template import loader
from .models import Account


def accounts(request):
  all_account = Account.objects.all().values()
  template = loader.get_template('all_account.html')
  context = {
    'all_account': all_account,
  }
  return HttpResponse(template.render(context, request))

def testing(request):
  data = Account.objects.filter(provider='HSBC', location="HK").values()
  template = loader.get_template('testing.html')
  context = {
    'data': data,
  }
  return HttpResponse(template.render(context, request))
