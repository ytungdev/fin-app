from django.shortcuts import render

def main(request):
  context = {}
  return render(request, 'main.html', context)

def testing(request):
  data = 'testing'
  context = {
    'data': data,
  }
  return render(request, 'testing.html', context)
