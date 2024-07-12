from django.shortcuts import render, redirect ,get_object_or_404
from .models import TasasCDAT, TasasCooviahorro
from .forms import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializer import CdatSerializer, CooviahorroSerializer
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def Admin(request):
    return render(request, 'options.html')

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
        

# Return all Cooviahorros controls
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

@login_required
def noSociales(request):
    nosociales = NoSociales.objects.all()
    return render(request, 'noSociales/noSociales.html', {'nosociales': nosociales})

@login_required
def createNoSociales(request):
    form = NoSocialesForm()
    if request.method == 'POST':
        form = NoSocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nosociales')
    return render(request, 'noSociales/createNoSociales.html', {'form': form})

@login_required
def updateNoSociales(request, id):
    nosocial = get_object_or_404(NoSociales, id=id)
    form = NoSocialesForm(instance=nosocial)
    if request.method == 'POST':
        form = NoSocialesForm(request.POST, instance=nosocial)
        if form.is_valid():
            form.save()
            return redirect('nosociales')
    return render(request, 'noSociales/updateNoSociales.html', {'form': form})

@login_required
def deleteNoSociales(request, id):
    nosocial = get_object_or_404(NoSociales, id=id)
    nosocial.delete()
    return redirect("nosociales")

@login_required
def typesAsociados(request):
    asociados = TypeAsociado.objects.all()
    form = TypesAsociadoForm()
    if request.method == 'POST':
        form = TypesAsociadoForm(request.POST)
        form.save()
        return redirect("asociados")
    return render(request, "asociados/asociados.html", {
        'asociados': asociados,
        'form': form})

@login_required
def createTypesAsociados(request):
    form = TypesAsociadoForm()
    if request.method == 'POST':
        form = TypesAsociadoForm(request.POST)
        form.save()
        return redirect("asociados")
    return render(request, "asociados/createAsociado.html", {
        'form': form})

@login_required
def deleteTypeAsociado(request, id):
    asociado = get_object_or_404(TypeAsociado, id=id)
    asociado.delete()
    return redirect("asociados")




@login_required
def tasasNoSociales(request):
    tasas = TasasNoSociales.objects.all()
    return render(request, 'tasas/tasasNoSociales.html', {'tasas': tasas})

@login_required
def createTasasNoSociales(request):
    form = TasasNoSocialesForm()
    if request.method == 'POST':
        form = TasasNoSocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasasnosociales')
    return render(request, 'tasas/createTasasNoSociales.html', {'form': form})

@login_required
def updateTasasNoSociales(request, id):
    tasa = get_object_or_404(TasasNoSociales, id=id)
    form = TasasNoSocialesForm(instance=tasa)
    if request.method == 'POST':
        form = TasasNoSocialesForm(request.POST, instance=tasa)
        if form.is_valid():
            form.save()
            return redirect('tasasnosociales')
    return render(request, 'tasas/updateTasasNoSociales.html', {'form': form})

@login_required
def deleteTasasNoSociales(request, id):
    tasa = get_object_or_404(TasasNoSociales, id=id)
    tasa.delete()
    return redirect("tasasnosociales")

class ApiCdat(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  CdatSerializer
    queryset = TasasCDAT.objects.all()
    

class ApiCooviahorro(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  CooviahorroSerializer
    queryset = TasasCooviahorro.objects.all()