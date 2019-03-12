from django.shortcuts import render
import requests
import json


def home(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)    

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    return render(request, 'home.html', {'api':api, 'price': price})

def price(request):
    # 어떤 입력값을 준 경우
    if request.method == 'POST':
        
        quote = request.POST['quote'] # form의 이름이 quote였으니까.
        quote = quote.upper()
        
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'price.html', {'quote':quote, 'crypto': crypto})
    
    # 페이지로 들어온 경우
    else:
        return render(request, 'price.html', {}) 

