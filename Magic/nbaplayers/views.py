from inspect import Parameter
from django.shortcuts import render
from nbaplayers.models import NBAplayer
def allplayersPage(request):
    allObjects = NBAplayer.objects.all()
    print(allObjects)
    slovar = {"players": allObjects}
    return render(request, "index2.html", slovar)

def CurrPlayer(request, playersname):
    selected = NBAplayer.objects.all().filter(playersname=playersname)
    character = selected[0]
    parameter = {"keyChar": character}
    return render(request, "Lebron.html", parameter)