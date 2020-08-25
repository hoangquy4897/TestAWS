from django.shortcuts import render

# Create your views here.


def helloworld(request):
    resp = render(request, 'index/index.html')
    resp['Cache-Control'] = 'public,max-age=100000'
    resp['Vary'] = 'Accept-Encoding'
    return resp