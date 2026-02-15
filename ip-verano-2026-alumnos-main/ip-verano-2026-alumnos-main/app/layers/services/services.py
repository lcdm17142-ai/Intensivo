# capa de servicio/lógica de negocio

import random
from ..transport import transport
from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user

def getAllImages():
    
    
    #Bruno. en esta lista llamamos a la funcion en la pagina "Trnsport" que es la que va a insertar
    #las imagenes desde otro lado 
    raw_images=transport.getAllImages()
    #Bruno. en esta parte llamo a la funcion que se encuentra en la pag "Translator" lo que hace es
    #transformar la imagen en tarjea o card les da el formato a la imagen llamada en la lista anterior
    cards=[translator.fromRequestIntoCard(img)for img in raw_images]
    
    #Bruno. aca retorna la tarjeta ya modificada con su imagen  
    return cards



def filterByCharacter(name):
    filtered_cards = []

    for card in getAllImages():
        # debe verificar si el name está contenido en el nombre de la card, antes de agregarlo al listado de filtered_cards.
        filtered_cards.append(card)

    return filtered_cards


def filterByStatus(status_name):
# función que filtra las cards según su estado.
    filtered_cards = [] 

    for card in getAllImages():
        if status_name in card.status:
    #Nico. agrego condicional que  evalua el parámetro en una lísta ["alive","deseaced", ...] la lista debeterer mas elementos
    # pero esos tres son los principales, si el estado esta contenido se agrega una carta a la lista de fichas filtradas
        # debe verificar si la casa de la card coincide con la recibida por parámetro. Si es así, se añade al listado de filtered_cards.
            filtered_cards.append(card)

    return filtered_cards

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    """
    Guarda un favorito en la base de datos.
    
    Se deben convertir los datos del request en una Card usando el translator,
    asignarle el usuario actual, y guardarla en el repositorio.
    """
    pass

def getAllFavourites(request):
    """
    Obtiene todos los favoritos del usuario autenticado.
    
    Si el usuario está autenticado, se deben obtener sus favoritos desde el repositorio,
    transformarlos en Cards usando translator y retornar la lista. Si no está autenticado, se retorna una lista vacía.
    """
    pass

def deleteFavourite(request):
    """
    Elimina un favorito de la base de datos.
    
    Se debe obtener el ID del favorito desde el POST y eliminarlo desde el repositorio.
    """
    pass