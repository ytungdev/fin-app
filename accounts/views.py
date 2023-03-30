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