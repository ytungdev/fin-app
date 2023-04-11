from django.shortcuts import render, redirect
from django.db.models import Sum

from .models import Stock, StockInOut, StockRecord
from .forms import StockForm
from datetime import date
import os
import csv


def format_symbol(sym):
    if sym.isdigit():
        res = sym.zfill(4)
    else:
        res = sym
    return res

def inouts(request):
    inout = StockInOut.objects.order_by('-date').values()
    stocks = []
    worths = []
    for rec in inout:
       stock = Stock.objects.filter(id=rec["stock_id"]).values()[0]
       stocks.append(stock)
       worths.append(rec["price"] * rec["unit"] * -1)
    print(stocks)
    context = {
        'data': zip(inout, stocks, worths),
    }
    return render(request, 'inouts.html', context)

def add_inout(request, stock_id=None):
  if request.method == 'POST':
    data = request.POST
    d =  data.get("date") if data.get("date") else date.today()
    #### debug
    print(data, stock_id)
    if stock_id==None:
        sym = format_symbol(data.get("symbol"))
        stock = Stock.objects.filter(symbol=sym).values()
        if not stock:        
            new = Stock()
            new.name = data.get("name").strip()
            new.symbol = sym
            new.market = data.get("market").upper()
            new.curr = data.get("curr").upper()
            new.save()
            stock_id = new.id
        else:
            stock_id = stock[0]["id"]
    
    rec = StockInOut.objects.filter(stock_id=stock_id, date=d).values()
    if rec:
       print(f"rec exist : {rec[0]['id']}")
    else:
        new = StockInOut()
        new.stock_id = stock_id
        new.date = d
        new.price = data.get("price")
        new.unit = data.get("unit")
        new.save()
        print(f"saved : {new.id}")
    return redirect(f'/stock/add_inout/{stock_id}')
  else:
    form = StockForm()
    if stock_id==None:
        context = { 'data' : None, 'form' : form}
        return render(request, 'add_stock_inout.html', context)
    else:
        stock = Stock.objects.filter(id=stock_id).values()
        if not stock:
            context = { 'data' : None, 'form' : form}
            return render(request, 'add_stock_inout.html', context)
        else:
            form.fields["market"].initial = stock[0]["market"]
            form.fields["symbol"].initial = stock[0]["symbol"]
            form.fields["name"].initial = stock[0]["name"]
            form.fields["curr"].initial = stock[0]["curr"]

            form.fields["market"].disabled = True
            form.fields["symbol"].disabled = True
            form.fields["name"].disabled = True
            form.fields["curr"].disabled = True

            inout = StockInOut.objects.filter(stock_id=stock_id).order_by('-date').values()
            worths = []
            gain = 0
            bal = 0
            for rec in inout:
                worth = rec["unit"] * rec["price"] * -1
                gain += worth
                bal += rec["unit"]
                worths.append(worth)
            
            # data = zip(inout, worths) if inout else None
            data = zip(inout, worths)
                
            context = {
                'stock_id':stock_id, 
                'form':form, 
                'data': data, 
                'gain': gain,
                'bal':bal
            }
            return render(request, 'add_stock_inout.html', context)
 
def load(request):
#   f = os.path.join('statics', 'secret', "cashrecords.csv")
#   with open(f, mode='r') as infile:
#     reader = csv.reader(infile)
#     for row in reader:
#       ac = Account.objects.filter(name=row[0].strip()).values()[0]
#       if ac:
#         a = ac["id"]
#         d = row[1].strip()
#         b = row[2].strip()
#         rec = CashRecord.objects.filter(account=a, date=d).values()
#         if rec:
#           print(f'record exist : {d} - {ac["name"]}')
#         else:
#           new_rec = CashRecord()
#           new_rec.account_id = a
#           new_rec.date = d
#           new_rec.balance = b
#           new_rec.save()
#       else:
#         print(f"account not exist : {row[0]}")
  return redirect('/dashboard')

