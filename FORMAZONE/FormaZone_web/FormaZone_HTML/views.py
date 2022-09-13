from django.shortcuts import render
from django.http import HttpResponse
from FormaZone_HTML.models import Widget
from django.core.paginator import Paginator

def Navigateur(request):
    Info = Widget.objects.all()
    paginator = Paginator(Info, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request,
                  'Html/FormaZone_recherche.html',
                  {"Info" : page_object ,
                   "Number_Post" : Info ,
                   "Page" : paginator,
                   "range" : range(1, paginator.num_pages + 1),
                   "range3": (paginator.num_pages - 2)})

def Resultat(request):
    search = request.GET.get('domaine_de_recherche')
    Info_filtre = Widget.objects.filter(Title__icontains=search)
    paginator = Paginator(Info_filtre, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request,
                  'Html/FormaZone_recherche_result.html',
                  { 'Info':page_object ,
                    "Number_Post": Info_filtre,
                    "search" : search,
                    "Page": paginator,
                    "range": range(1, 1 + paginator.num_pages),
                    "range3": (paginator.num_pages - 2)})


def Accueil(request):
    return render(request,
                  'Html/Accueil.html')
