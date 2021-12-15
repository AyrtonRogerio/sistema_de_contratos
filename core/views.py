from django.http import JsonResponse

def empresas(request):
    if request.method == 'GET':
        empresa = {'id':1,'nome':'Serra Bela','cnpj':12345678910112}
        return JsonResponse(empresa)
