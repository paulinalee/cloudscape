from django.http import HttpResponse
from django.shortcuts import render

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')

def home(request):
    return render(request, 'home.html')