from django.shortcuts import render
from django.http import HttpResponse
import json

def index(request):
    with open('phone.json', 'r') as f:
        data = json.load(f)

    with open('marque.json', 'r') as f:
        brands = json.load(f)

    selected_brand = request.GET.get('brand', None)
    selected_price = request.GET.get('price', None)

    filtered_data = []
    for item in data:
        if selected_brand is not None and item['marque'] != selected_brand:
            continue
        item['price'] = item['price'].split()[0]

        if selected_price is not '' and float(item['price'].replace(',', '')) > float(selected_price):
            print(item)
            continue

        filtered_data.append(item)

    context = {
        'data': filtered_data,
        'brands': brands,
        'selected_brand': selected_brand,
        'selected_price': selected_price,
    }
    return render(request, 'index.html', context)
