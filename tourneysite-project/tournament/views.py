from django.shortcuts import render

# Create your views here.
def dashboard(request) :
    return render(request, 'tournament/dashboard.html')

def create_tournament(request) :
    return render(request, 'tournament/create_tournament.html')