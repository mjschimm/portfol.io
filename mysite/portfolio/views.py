from django.shortcuts import render

def index(request):
	return render(request, "pio_home.html")

def new_profile1(request):
    return render(request, "new_profile1.html")

def edit_profile(request):
    return render(request, "edit_profile.html")
def post_view(request):
    return render(request, "post_view.html")
  
def post_edit(request):
    return render(request, "post_edit.html")

