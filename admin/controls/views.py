from django.shortcuts import render, redirect ,get_object_or_404
from .models import TasasCDAT, TasasCooviahorro
from .forms import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status, views
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def Admin(request):
    return render(request, 'options.html')

@login_required
def creditos(request):
    return render(request, 'creditos/controls.html')

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


class ApiCdat(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  CdatSerializer
    queryset = TasasCDAT.objects.all()
    

class ApiCooviahorro(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class =  CooviahorroSerializer
    queryset = TasasCooviahorro.objects.all()

class SimuladorCreditoApiView(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Obtener datos de ApiCdat
        noSociales = NoSocialesSerializer(NoSociales.objects.all(), many=True).data
        sociales = SocialesSerializer(Sociales.objects.all(), many=True).data
        fidelizacion = FidelizacionSerializer(Fidelizacion.objects.all(), many=True).data
        tasasNoSociales = TasasSerializer(TasasNoSociales.objects.all(), many=True).data
        ajusteScore = AjustesScoreSerializer(AjustesScore.objects.all(), many=True).data
        ajusteAporte = AjustesAportesSerializer(AjustesAportes.objects.all(), many=True).data
        ajustePlazo = AjustesPlazoSerializer(AjustesPlazo.objects.all(), many=True).data
        ajusteCdat = AjustesCdatSerializer(AjustesCDAT.objects.all(), many=True).data
        ajusteCooviahorro = AjustesCooviahorroSerializer(AjustesCooviahorro.objects.all(), many=True).data
        maximoAjuste = MaximoAjusteSerializer(MaximoAjuste.objects.all(), many=True).data
        asociadoType = TypeAsociadoSerializer(TypeAsociado.objects.all(), many=True).data
        
        data = {
            'salariominimo': 1462000,
            'nosociales': noSociales,
            'sociales': sociales,
            'fidelizacion': fidelizacion,
            'tasasnosociales': tasasNoSociales,
            'maximoDescuento': maximoAjuste,
            'tiposAsociados': asociadoType,
            'descuentos': {
                'score': ajusteScore,
                'aporte': ajusteAporte,
                'plazo': ajustePlazo,
                'cdat': ajusteCdat,
                'cooviahorro': ajusteCooviahorro
            }
        }
        
        return Response(data, status=status.HTTP_200_OK)