from django.shortcuts import render

def index(request):
	return render(request, "pio_home.html")

def new_profile1(request):
    return render(request, "new_profile1.html")
