from django.shortcuts import render
from .models import Team

def teamslist(request):
    items = Team.objects.all()
    return render(request, 'TeamPlayer.html', {'items':items})
