from django.shortcuts import render
from .models import lora
from django.views.generic.edit import UpdateView
from django.http import JsonResponse, HttpResponseRedirect

def leituraView(request):
    try:
        filtro = request.POST['dia']
        leitura_completa = lora.objects.filter(dataleitura__day=filtro).all().order_by("-dataleitura")

        # leitura_completa = leitura_completa.reverse()[(len(leitura_completa)-10):len(leitura_completa)]
    except:
        leitura_completa = lora.objects.all().order_by("-dataleitura")[1:10]

    context = {"all_items": leitura_completa}
    return render(request,'todo.html',context)



class AuthorUpdate(UpdateView):
    model = lora
    template_name_suffix = '_update_formulario'
