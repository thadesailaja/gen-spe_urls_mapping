from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def topcar(request):
    return HttpResponse('''<h1><i>Volkswagen is a top car manufacturer from Germany!!!</i></h1>
                        <img src="https://motownindia.com/images/Auto-Industry/Volkswagen-recalls-800000-cars-in-Germany-for-rectifying-emission-glitches-Motown-India-Bureau-1-982.jpg" width="250px">''')