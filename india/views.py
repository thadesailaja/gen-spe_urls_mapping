from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def topcar(request):
    return HttpResponse('''<h1>Maruti Suzuki is a top car manufacturer from INDIA</h1>
                        <img src="https://www.financialexpress.com/wp-content/uploads/2022/10/2022-Maruti-Suzuki-Baleno-Facelift-1-1.webp?w=1024" width="250px">''')
def sectopcar(request):
    return HttpResponse('''<h1>Tata Punch is a second top car manufacturer from INDIA</h1>
                        <img src="https://imgd.aeplcdn.com/1200x900/n/cw/ec/39015/punch-exterior-right-front-three-quarter-54.jpeg?isig=0&q=80" width="250px">''')