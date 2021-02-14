from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import BadHabbitForm, SubsForm
from .models import BadHabbit, Subs
def index(request):
    return render(request, 'out/index.html')

def create(request):
    if request.method == 'POST':
        dangers = request.POST.getlist('dangers')
        title = request.POST.get('title')
        descri = request.POST.get('description')
        form = BadHabbitForm(
                {
                    'dangers': dangers, 
                    'title': title, 
                    'description': descri
                }
            )
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': "Data saved"
            })
        else:
            return JsonResponse({
                form.errors
            })


def bad(request, bad_id):
     bad = BadHabbit.objects.get(pk=bad_id)
     context = {
         'bad': bad
     }
     
     return render(request, 'out/show.html', context)
def subs(request, bad_id):
    return render(request, 'out/create_subs.html', {'bad_id': bad_id})

def subs_create(request, bad_id):
    if request.method == 'POST':
        form = SubsForm(
                {
                    'title' : request.POST.get('title'),
                    'description' : request.POST.get('description'),
                    'badget_min' : request.POST.get('badget_min'),
                    'badget_max' : request.POST.get('badget_max'),
                    'efficacite' : request.POST.get('efficacite'),
                    'duration' : request.POST.get('duration'),
                    'bad_id' : BadHabbit.objects.get(pk=bad_id)
                }
            )
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': "Data saved"
            })
        else:
            return JsonResponse({
                'success': False,
                'errors': dict(form.errors.items()),
            })

