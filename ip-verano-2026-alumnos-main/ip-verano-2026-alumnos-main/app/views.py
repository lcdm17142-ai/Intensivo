# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from app.layers.services.services import filterByStatus
#Noelia B. Importamos la función desdes services.py , para ello hay que escribir todas las rutas desde la rama principal
#hasta llegar al archivo donde esta la funcion que necesitamos 

#Candela Gullo: Importa el modelo User de Django, que representa a los usuarios registrados en la aplicacion.
from django.contrib.auth.models import User

#Candela Gullo: Permite mostrar mensajes tipo alerta en la web (por ejemplo, mensajes de éxito o error).
from django.contrib import messages

#Candela Gullo: Te da acceso a la configuración del proyecto (settings.py).
from django.conf import settings

#Candela Gullo: Función integrada de Django para enviar correos electrónicos desde el servidor.
from django.core.mail import send_mail

#Candela Gullo: Importa el modelo Favourite desde el archivo models.py que está en el mismo modulo por eso el punto . al comienzo.
from app.models import Favourite


def index_page(request):
    return render(request, 'index.html')

def home(request):
        #Bruno. hice que la lista retorne las tarjetas modificadas y definidas en la pag "Services"
    images= services.getAllImages()
     #Bruno: esta lista va a retornar los favoritos del usuario
    favourites = getAllFavouritesByUser(request)

    #runo: retorna las imagenes en la pagina "home.html"
    return render(request, 'home.html', {'images': images,'favourites': favourites})

    



def search(request):
    name = request.POST.get('query', '')

    #Candela Gullo: si el usuario ingresó algo en el buscador, se deben filtrar las imágenes por dicho ingreso.
    if (name != ''):
        images = services.getAllImages()
        
    #Candela Gullo: filtra por nombre parcial ignorando mayúsculas/minúsculas
        images = [img for img in images if name in img.name.lower()]

        return render(request, 'home.html', { 'images': images})
    else:
        return redirect('home')


def filter_by_status(request):
    status = request.POST.get('status', '')

    if status != '':
#Nico. tengo que importar la funcion filterByStatus del archivo services.py que retorta card filtradas 
        images = filterByStatus (status) # debe traer un listado filtrado de imágenes, segun si es o contiene ese estado.
        favourite_list = []

        return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })
    else:
        return redirect('home')
#Nico. Esta Funcion (filter_by_status) luego usada en "home.html" va a permitir que los botones de calsificacion "vivo" "fallecido" se ejecuten

# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    """
    pass

@login_required
def saveFavourite(request):
    """
    Guarda un personaje como favorito.
    """
    pass

@login_required
def deleteFavourite(request):
    """
    Elimina un favorito del usuario.
    """
    pass

@login_required
def exit(request):
    logout(request)
    return redirect('home')