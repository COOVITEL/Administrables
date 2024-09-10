from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import *
from .forms import *

@login_required
def controlRotativos(request):
    return render(request, 'rotativos/controls.html')

@login_required
def rotativos(request):
    rotativos = Rotativo.objects.all()
    return render(request, 'rotativos/rotativos.html', {'rotativos': rotativos})

@login_required
def createRotativo(request):
    form = RotativoForm()
    if request.method == 'POST':
        form = RotativoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rotativos')
    return render(request, 'rotativos/createrotativo.html', {'form': form})

@login_required
def updateRotativo(request, id):
    rotativo = get_object_or_404(Rotativo, id=id)
    form = RotativoForm(instance=rotativo)
    if request.method == 'POST':
        form = RotativoForm(request.POST, instance=rotativo)
        if form.is_valid():
            form.save()
            return redirect('rotativos')
    return render(request, 'rotativos/updaterotativo.html')

@login_required
def deleteRotativo(request, id):
    rotativo = get_object_or_404(Rotativo, id=id)
    rotativo.delete()
    return redirect('rotativos')



@login_required
def escenarios(request):
    escenarios = Escenarios.objects.all()
    return render(request, 'rotativos/escenarios/escenarios.html', {'escenarios': escenarios})

@login_required
def createEscenarios(request):
    form = EscenariosForm()
    if request.method == 'POST':
        form = EscenariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('escenarios')
    return render(request, 'rotativos/escenarios/createescenarios.html', {'form': form})

@login_required
def updateEscenarios(request, id):
    escenarios = get_object_or_404(Escenarios, id=id)
    form = EscenariosForm(instance=escenarios)
    if request.method == 'POST':
        form = EscenariosForm(request.POST, instance=escenarios)
        if form.is_valid():
            form.save()
            return redirect('escenarios')
    return render(request, 'rotativos/escenarios/updateescenarios.html', {"form": form})

@login_required
def deleteEscenarios(request, id):
    escenarios = get_object_or_404(Escenarios, id=id)
    escenarios.delete()
    return redirect('escenarios')