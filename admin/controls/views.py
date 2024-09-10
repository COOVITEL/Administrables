from django.shortcuts import render, redirect ,get_object_or_404
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