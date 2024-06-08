from django.shortcuts import render
import random
def index(request):
    liters = list ('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercase'):
        liters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')
    if request.GET.get('spicial'):
        liters.extend('!@#$%^&*()№?;:,./|')
    if request.GET.get('number'):
        liters.extend('1234567890')
    lenght = int (request.GET.get('lenght', 16))
    thepassword = ''
    for i in range (lenght):
        thepassword += random.choice(liters)
    return render(request, 'generator1/index.html', {'password':thepassword})

def about(request):
    return render(request, 'generator1/about.html')