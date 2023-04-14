from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.views import generic
from django.contrib import messages

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


class StockList(generic.ListView):
    template_name = 'stock_list.html'
    context_object_name = 'all_stock'

    def get_queryset(self):
        return Stock.objects.all()


def view_stock(request, stock_id=None):
    # recieve form
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            symbol = format_symbol(form.cleaned_data['symbol'])
            market = form.cleaned_data['market'].upper()
            # create new stock
            if stock_id == None:
                stock = Stock.objects.filter(symbol=symbol, market=market).values()
                # reject : stock exists
                if stock:
                    messages.error(request, f'stock exist : {stock[0]["symbol"]}')
                    return redirect('/stock/view_stock')
                else:
                    stock = Stock()
            # update existing stock
            else:
                stock = get_object_or_404(Stock, pk=stock_id)
            stock.market = market
            stock.symbol = symbol
            stock.name = form.cleaned_data['name']
            stock.curr = form.cleaned_data['curr'].upper()
            stock.save()
            return redirect('/stock/stocks')
    # render form
    else:
        form = StockForm()
        # blank form
        if stock_id == None:
            stock = None
        # fetched form
        else:
            stock = get_object_or_404(Stock, pk=stock_id)
            form.fields["market"].initial = stock.market
            form.fields["symbol"].initial = stock.symbol
            form.fields["name"].initial = stock.name
            form.fields["curr"].initial = stock.curr
        context = {'form': form, 'data': stock}
        return render(request, 'stock_details.html', context)


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
    # recieve form
    if request.method == 'POST':
        data = request.POST
        d = data.get("date") if data.get("date") else date.today()

        # create new stock
        if stock_id == None:
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
                messages.error(request, f'stock exist : {stock[0]["symbol"]}')
                stock_id = stock[0]["id"]
                return redirect(f"stock/add_inout/{stock_id}")

        # create new reocrd
        rec = StockInOut.objects.filter(stock_id=stock_id, date=d).values()
        if rec:
            messages.error(
                request, f'record exist : {d} - {stock_id} - {rec[0]["id"]} ')
        else:
            new = StockInOut()
            new.stock_id = stock_id
            new.date = d
            new.price = data.get("price")
            new.unit = data.get("unit")
            new.save()
            print(f"saved : {new.id}")
        return redirect(f'/stock/add_inout/{stock_id}')
    # render form
    else:
        form = StockForm()
        # blannk form
        if stock_id == None:
            context = {'data': None, 'form': form}
            return render(request, 'add_stock_inout.html', context)
        # fetched form
        else:
            stock = get_object_or_404(Stock, pk=stock_id)
            form.fields["market"].initial = stock.market
            form.fields["symbol"].initial = stock.symbol
            form.fields["name"].initial = stock.name
            form.fields["curr"].initial = stock.curr

            form.fields["market"].disabled = True
            form.fields["symbol"].disabled = True
            form.fields["name"].disabled = True
            form.fields["curr"].disabled = True

            inout = StockInOut.objects.filter(
                stock_id=stock_id).order_by('-date').values()
            worths = []
            gain, bal = 0, 0
            for rec in inout:
                worth = rec["unit"] * rec["price"] * -1
                gain += worth
                bal += rec["unit"]
                worths.append(worth)

            # data = zip(inout, worths) if inout else None
            data = zip(inout, worths)

            context = {
                'stock_id': stock_id,
                'form': form,
                'data': data,
                'gain': gain,
                'bal': bal
            }
            return render(request, 'add_stock_inout.html', context)

def add_record(request):
    stocks = Stock.objects.order_by('market').all()
    # recieve form
    if request.method == 'POST':
        data = request.POST
        # print(data)
        for curr in currs:
            res = data.get(f"rate_{curr}")
            d = data.get("date") if data.get("date") else date.today()
            if res:
                # new entry to db
                new_rec = StockRecord()
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
        prev_prices = []
        for stock in stocks:
            prev_rec = StockRecord.objects.filter(stock_id=stock.id).order_by('-date').values()
            if prev_rec:
                prev_prices.append(prev_rec[0]['price'])
            else:
                prev_prices.append("")
        context = {
            'stocks': zip(stocks, prev_prices)
        }
        # print(zip(currs, prev_rate))
        return render(request, 'add_stock_record.html', context)

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
