from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from django.shortcuts import get_object_or_404, redirect
from .forms import *


@login_required
def ajustesScore(request):
    ajustes = AjustesScore.objects.all()
    return render(request, 'creditos/ajustes/score/ajustesscore.html', {'ajustes': ajustes})

@login_required
def createAjustesScore(request):
    form = AjustesScoreForm()
    if request.method == 'POST':
        form = AjustesScoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajustescore')
    return render(request, 'creditos/ajustes/score/createajustescore.html', {'form': form})

@login_required
def updateAjustesScore(request, id):
    ajuste = get_object_or_404(AjustesScore, id=id)
    form = AjustesScoreForm(instance=ajuste)
    if request.method == 'POST':
        form = AjustesScoreForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            return redirect('ajustescore')
    return render(request, 'creditos/ajustes/score/updateajustescore.html', {'form': form})

@login_required
def deleteAjustesScore(request, id):
    ajuste = get_object_or_404(AjustesScore, id=id)
    ajuste.delete()
    return redirect('ajustescore')

@login_required
def ajustesAporte(request):
    ajustes = AjustesAportes.objects.all()
    return render(request, 'creditos/ajustes/aporte/ajustesaporte.html', {'ajustes': ajustes})

@login_required
def createAjustesAporte(request):
    form = AjustesAportesForm()
    if request.method == 'POST':
        form = AjustesAportesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajusteaporte')
    return render(request, 'creditos/ajustes/aporte/createajustesaporte.html', {'form': form})

@login_required
def updateAjustesAporte(request, id):
    ajuste = get_object_or_404(AjustesAportes, id=id)
    form = AjustesAportesForm(instance=ajuste)
    if request.method == 'POST':
        form = AjustesAportesForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            return redirect('ajusteaporte')
    return render(request, 'creditos/ajustes/aporte/updateajustesaporte.html', {'form': form})

@login_required
def deleteAjustesAporte(request, id):
    ajuste = get_object_or_404(AjustesAportes, id=id)
    ajuste.delete()
    return redirect('ajusteaporte')

@login_required
def ajustesPlazo(request):
    ajustes = AjustesPlazo.objects.all()
    return render(request, 'creditos/ajustes/plazo/ajustesplazo.html', {'ajustes': ajustes})

@login_required
def createAjustesPlazo(request):
    form = AjustesPlazoForm()
    if request.method == 'POST':
        form = AjustesPlazoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajusteplazo')
    return render(request, 'creditos/ajustes/plazo/createajustesplazo.html', {'form': form})

@login_required
def updateAjustesPlazo(request, id):
    ajuste = get_object_or_404(AjustesPlazo, id=id)
    form = AjustesPlazoForm(instance=ajuste)
    if request.method == 'POST':
        form = AjustesPlazoForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            return redirect('ajusteplazo')
    return render(request, 'creditos/ajustes/plazo/updateajustesplazo.html', {'form': form})

@login_required
def deleteAjustesPlazo(request, id):
    ajuste = get_object_or_404(AjustesPlazo, id=id)
    ajuste.delete()
    return redirect('ajusteplazo')

@login_required
def ajustesCDAT(request):
    ajustes = AjustesCDAT.objects.all()
    return render(request, 'creditos/ajustes/cdat/ajustescdat.html', {'ajustes': ajustes})

@login_required
def createAjustesCDAT(request):
    form = AjustesCDATForm()
    if request.method == 'POST':
        form = AjustesCDATForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajustecdat')
    return render(request, 'creditos/ajustes/cdat/createajustescdat.html', {'form': form})

@login_required
def updateAjustesCDAT(request, id):
    ajuste = get_object_or_404(AjustesCDAT, id=id)
    form = AjustesCDATForm(instance=ajuste)
    if request.method == 'POST':
        form = AjustesCDATForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            return redirect('ajustecdat')
    return render(request, 'creditos/ajustes/cdat/updateajustescdat.html', {'form': form})

@login_required
def deleteAjustesCDAT(request, id):
    ajuste = get_object_or_404(AjustesCDAT, id=id)
    ajuste.delete()
    return redirect('ajustecdat')



@login_required
def ajustesCooviahorro(request):
    ajustes = AjustesCooviahorro.objects.all()
    return render(request, 'creditos/ajustes/cooviahorro/ajustescooviahorro.html', {'ajustes': ajustes})

@login_required
def createAjustesCooviahorro(request):
    form = AjustesCooviahorroForm()
    if request.method == 'POST':
        form = AjustesCooviahorroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ajustecooviahorro')
    return render(request, 'creditos/ajustes/cooviahorro/createajustescooviahorro.html', {'form': form})

@login_required
def updateAjustesCooviahorro(request, id):
    ajuste = get_object_or_404(AjustesCooviahorro, id=id)
    form = AjustesCooviahorroForm(instance=ajuste)
    if request.method == 'POST':
        form = AjustesCooviahorroForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            return redirect('ajustecooviahorro')
    return render(request, 'creditos/ajustes/cooviahorro/updateajustescooviahorro.html', {'form': form})

@login_required
def deleteAjustesCooviahorro(request, id):
    ajuste = get_object_or_404(AjustesCooviahorro, id=id)
    ajuste.delete()
    return redirect('ajustecooviahorro')

@login_required
def descuentos(request):
    descuentos = MaximoAjuste.objects.all()
    return render(request, 'creditos/ajustes/descuentos/descuentos.html', {'descuentos': descuentos})

@login_required
def createDescuentos(request):
    form = MaximoAjustesForm()
    if request.method == 'POST':
        form = MaximoAjustesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('descuentos')
    return render(request, 'creditos/ajustes/descuentos/createdescuentos.html', {'form': form})

@login_required
def updateDescuentos(request, id):
    ajuste = get_object_or_404(MaximoAjuste, id=id)
    form = MaximoAjustesForm(instance=ajuste)
    if request.method == 'POST':
        form = MaximoAjustesForm(request.POST, instance=ajuste)
        if form.is_valid():
            form.save()
            return redirect('descuentos')
    return render(request, 'creditos/ajustes/descuentos/updatedescuentos.html', {'form': form})

@login_required
def deleteDescuentos(request, id):
    ajuste = get_object_or_404(MaximoAjuste, id=id)
    ajuste.delete()
    return redirect('descuentos')