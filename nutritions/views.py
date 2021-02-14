from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from apis import Nutrition
from .models import nutritions
from django.template import loader

# Create your views here.

def index(request):
    nutritions_list = nutritions.objects.all()
    template = loader.get_template('index.html')
    context = {
        'nutritions_list': nutritions_list,
    }
    return HttpResponse(template.render(context, request)) 

def detail(request, nutritions_id):
    nutr = nutritions.objects.get(pk=nutritions_id)
    template = loader.get_template('show.html')
    context = {
        'nutrition': nutr,
    }
    return HttpResponse(template.render(context, request)) 

def fetch(request):
    n = Nutrition()
    data = n.data('beef')
    for dic in data:
        nutr = nutritions()
        nutr.__dict__.update(dic)
        nutr.save()
    
    alls = nutritions.objects.all()
    listOfElems = []
    duplic = []

    for i in range(0, len(alls)-1):
        listOfElems.append(alls[i].foodid)

    setOfElems = set()
    
    for elem in listOfElems:
        if elem in setOfElems:
            duplic.append(elem)
        else:
            setOfElems.add(elem) 
    for foodid in duplic:
        nu = nutritions.objects.filter(foodid=foodid)
        nu.delete()

    return JsonResponse({
        'message': 'Data fetched successfully'
    })
    

def dupli(request):
    alls = nutritions.objects.all()
    listOfElems = []
    duplic = []

    for i in range(0, len(alls)-1):
        listOfElems.append(alls[i].foodid)

    setOfElems = set()

    for elem in listOfElems:
        if elem in setOfElems:
            duplic.append(elem)
        else:
            setOfElems.add(elem)         
    
    for foodid in duplic:
        nu = nutritions.objects.filter(foodid=foodid)
        nu.delete()

    return HttpResponse(len(duplic))


