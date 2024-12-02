from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'face_to_site/home.html')

def open_to_fairi_tales(requst):
    return render(requst,'face_to_site/open_to_fairi_tales.html')