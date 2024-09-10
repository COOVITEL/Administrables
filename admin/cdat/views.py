from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .models import *
from .forms import *


@login_required
def Cdat(request):
    cdats = TasasCDAT.objects.all()
    return render(request, 'cdats/cdat.html', {'cdats': cdats})

@login_required
def createCdat(request):
    form = TasasCDATForm()
    if request.method == 'POST':
        form = TasasCDATForm(request.POST)
        if form.is_valid():
            form.save()        
            return redirect('cdats')
    return render(request, 'cdats/createcdat.html', {'form': form})

@login_required
def updatecdat(request, id):
    cdat = get_object_or_404(TasasCDAT, id=id)
    form = TasasCDATForm(instance=cdat)
    if request.method == 'POST':
        form = TasasCDATForm(request.POST, instance=cdat)
        if form.is_valid():
            form.save()
            return redirect('cdats')
    return render(request, 'cdats/updatecdat.html', {'form': form})

@login_required
def deletecdat(request, id):
    cdat = get_object_or_404(TasasCDAT, id=id)
    cdat.delete()
    return redirect('cdats')