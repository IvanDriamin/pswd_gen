from django.shortcuts import render
import random
def index(request):
    liters = list ('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        liters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if request.GET.get('special'):
        liters.extend('!@#$%^&*()№?;:,./|')
    if request.GET.get('number'):
        liters.extend('1234567890')
    lenght = int (request.GET.get('lenght', 8))
    thepassword = ''
    for i in range (lenght):
        thepassword += random.choice(liters)
    return render(request, 'generator1/index.html', {'password':thepassword})

def password(request):
    return render(request, 'generator1/password.html')

def about(request):
    return render(request, 'generator1/about.html')