from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404, redirect

@login_required
def noSociales(request):
    nosociales = NoSociales.objects.all()
    return render(request, 'creditos/noSociales/noSociales.html', {'nosociales': nosociales})

@login_required
def createNoSociales(request):
    form = NoSocialesForm()
    if request.method == 'POST':
        form = NoSocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nosociales')
    return render(request, 'creditos/noSociales/createNoSociales.html', {'form': form})

@login_required
def updateNoSociales(request, id):
    nosocial = get_object_or_404(NoSociales, id=id)
    form = NoSocialesForm(instance=nosocial)
    if request.method == 'POST':
        form = NoSocialesForm(request.POST, instance=nosocial)
        if form.is_valid():
            form.save()
            return redirect('nosociales')
    return render(request, 'creditos/noSociales/updateNoSociales.html', {'form': form})

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
    return render(request, "creditos/asociados/asociados.html", {
        'asociados': asociados,
        'form': form})

@login_required
def createTypesAsociados(request):
    form = TypesAsociadoForm()
    if request.method == 'POST':
        form = TypesAsociadoForm(request.POST)
        form.save()
        return redirect("asociados")
    return render(request, "creditos/asociados/createAsociado.html", {
        'form': form})

@login_required
def deleteTypeAsociado(request, id):
    asociado = get_object_or_404(TypeAsociado, id=id)
    asociado.delete()
    return redirect("asociados")

@login_required
def tasasNoSociales(request):
    tasas = TasasNoSociales.objects.all()
    return render(request, 'creditos/tasas/tasasNoSociales.html', {'tasas': tasas})

@login_required
def createTasasNoSociales(request):
    form = TasasNoSocialesForm()
    if request.method == 'POST':
        form = TasasNoSocialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasasnosociales')
    return render(request, 'creditos/tasas/createTasasNoSociales.html', {'form': form})

@login_required
def updateTasasNoSociales(request, id):
    tasa = get_object_or_404(TasasNoSociales, id=id)
    form = TasasNoSocialesForm(instance=tasa)
    if request.method == 'POST':
        form = TasasNoSocialesForm(request.POST, instance=tasa)
        if form.is_valid():
            form.save()
            return redirect('tasasnosociales')
    return render(request, 'creditos/tasas/updateTasasNoSociales.html', {'form': form})

@login_required
def deleteTasasNoSociales(request, id):
    tasa = get_object_or_404(TasasNoSociales, id=id)
    tasa.delete()
    return redirect("tasasnosociales")

@login_required
def fidelizacion(request):
    fidelizacion = Fidelizacion.objects.all()
    return render(request, 'creditos/fidelizacion/fidelizacion.html', {'fidelizacion': fidelizacion})

@login_required
def createfidelizacion(request):
    form = FidelizacionForm()
    if request.method == 'POST':
        form = FidelizacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fidelizacion')
    return render(request, 'creditos/fidelizacion/createfidelizacion.html', {'form': form})

@login_required
def updatefidelizacion(request, id):
    fidelizacion = get_object_or_404(Fidelizacion, id=id)
    form = FidelizacionForm(instance=fidelizacion)
    if request.method == 'POST':
        form = FidelizacionForm(request.POST, instance=fidelizacion)
        if form.is_valid():
            form.save()
            return redirect('fidelizacion')
    return render(request, 'creditos/fidelizacion/updatefidelizacion.html', {'form': form})

@login_required
def deletefidelizacion(request, id):
    fidelizacion = get_object_or_404(Fidelizacion, id=id)
    fidelizacion.delete()
    return redirect('fidelizacion')

@login_required
def sociales(request):
    social = Sociales.objects.all()
    return render(request, 'creditos/sociales/sociales.html', {'social': social})

@login_required
def createsociales(request):
    form = SolcialesForm()
    if request.method == 'POST':
        form = SolcialesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sociales')
    return render(request, 'creditos/sociales/createsociales.html', {'form': form})

@login_required
def updatesociales(request, id):
    social = get_object_or_404(Sociales, id=id)
    form = SolcialesForm(instance=social)
    if request.method == 'POST':
        form = SolcialesForm(request.POST, instance=social)
        if form.is_valid():
            form.save()
            return redirect('sociales')
    return render(request, 'creditos/sociales/updatesociales.html', {'form': form})

@login_required
def deletesociales(request, id):
    social = get_object_or_404(Sociales, id=id)
    social.delete()
    return redirect('sociales')



@login_required
def asociadosType(request):
    asociados = AsociadoType.objects.all()
    return render(request, 'creditos/asociadosType/asociados.html', {'asociados': asociados})

@login_required
def createasociadosType(request):
    form = AsociadoTypeForm()
    if request.method == 'POST':
        form = AsociadoTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asociadostype')
    return render(request, 'creditos/asociadosType/createasociados.html', {'form': form})

@login_required
def deleteasociadosType(request, id):
    asociado = get_object_or_404(AsociadoType, id=id)
    asociado.delete()
    return redirect('asociados')