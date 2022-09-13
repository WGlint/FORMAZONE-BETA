
from django.contrib import admin
from django.urls import path
from FormaZone_HTML import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Accueil/', views.Accueil, name="Accueil"),
    path('Recherche/', views.Navigateur, name="Recherche"),
    path('Resultat/', views.Resultat, name="Resultat"),
]
