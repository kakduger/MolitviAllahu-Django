from django.shortcuts import render

def initPage(request):
    return render(request, "index2.html")
    
