 # AllCode/views.py  
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import JsonResponse

import urllib.request, json
import os
os.getcwd() 

def search_all_data(request):
    searchquery = request.GET.get('searchquery', None)
    with open(r'/Users/innovatie/Desktop/Software-Trajecten/Django-Projects/Intents_id_all_subbed.json') as f:
        data = json.load(f)

    intentlist = []

    for item in data:
        cluster = ""
        cluster = item['label'].replace("/","_")
    #cluster = re.sub(r'\([^)]*\)', '', cluster)
        if cluster == searchquery:
            for intents in item['groups']:
                intentid = item['groups'].index(intents)
                intentlabel = intents['label']
                intenttuple = ((intentlabel, searchquery))
                intentlist.append(intenttuple)
    data = intentlist[:10]
    
    return JsonResponse(data, safe=False)

def get_action(request):
    #Deze functie bewerken
    intentid = request.GET.get('intentid', None)
    searchquery = request.GET.get('searchquery', None)

    with open(r'/Users/innovatie/Desktop/Software-Trajecten/Django-Projects/Intents_id_all_subbed.json') as f:
        data = json.load(f)

    intentlist = []

    for item in data:
        for intent in item['groups']:
            if(intent['label']) == intentid:
                #vul hier de relevante data in. Onderstaande is dummy
                for action in intent['groups'][:10]:
                    intenttuple = (action['label'], 11)
                    intentlist.append(intenttuple)
                    data = intentlist

    return JsonResponse(data, safe=False)

def post_feedback(request):
    #Post functie maken dat de weigth kolom gevult word in de json file a.d.h.v. de geklikte button. True = +1 en False = -1 weigth
    return True

# Create your views here.
class HomePageView(TemplateView):
    template_name="index.html"