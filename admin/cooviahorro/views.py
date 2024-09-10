from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import *
from .forms import *


@login_required
def Cooviahorro(request):
    ahorros = TasasCooviahorro.objects.all()
    return render(request, 'cooviahorro/cooviahorro.html', {'ahorros': ahorros})

@login_required
def createCooviahorro(request):
    form = TasasCooviahorroForm()
    if request.method == 'POST':
        form = TasasCooviahorroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cooviahorro')
    return render(request, 'cooviahorro/createcooviahorro.html', {'form': form})

# Get cooviahorro
@login_required
def updatecooviahorro(request, id):
    cooviahorro = get_object_or_404(TasasCooviahorro, id=id)
    form = TasasCooviahorroForm(instance=cooviahorro)
    if request.method == 'POST':
        form = TasasCooviahorroForm(request.POST, instance=cooviahorro)
        if form.is_valid():
            form.save()
            return redirect('cooviahorro')      
    return render(request, 'cooviahorro/updatecooviahorro.html', {'form': form})

@login_required
def deletecooviahorro(request, id):
    cooviahoroo = get_object_or_404(TasasCooviahorro, id=id)
    cooviahoroo.delete()
    return redirect("cooviahorro")