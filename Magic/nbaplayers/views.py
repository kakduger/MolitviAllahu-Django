from django.shortcuts import render
from nbaplayers.models import NBAplayer
def allplayersPage(request):
    allObjects = NBAplayer.objects.all()
    print(allObjects)
    slovar = {"players": allObjects}
    return render(request, "index2.html", slovar)

def CurrPlayer(request):
    return "Current Player"