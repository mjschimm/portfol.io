from django.shortcuts import render

def index(request):
	return render(request, "pio_home.html")

def new_profile1(request):
    return render(request, "new_profile1.html")

def edit_profile(request):
    return render(request, "edit_profile.html")
