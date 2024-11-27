from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def kortopcar(request):
    return HttpResponse('''<h1>Hyundai is a top car manufacturer from South Korea</h1>
                        <img src="https://hanshyundai.com/offer/tucson.png" width="250px">''')

def skortopcar(request):
    return HttpResponse('''<h1>Kia Carnival is a second top car manufacturer from South Korea</h1>
                        <img src="https://imgd-ct.aeplcdn.com/664x415/n/cw/ec/41205/carnival-exterior-left-front-three-quarter-2.jpeg?isig=0&q=80" width="250px">''')