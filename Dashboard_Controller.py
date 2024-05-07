from django.shortcuts import render

def display_Dashboard(request):
    return render(request,"Dashboard.html")