# -*- coding: utf-8 -*-
"""Alnago.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/117XZk2bEq-6SOYSKtL24St-xDCpbiYD5
"""

from time import time, sleep
import datetime
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def validate_zone(barrio):
  zonaEncontrada = False
  zona = None
  Nororiental = ["Nororiental", "El Chagualo", "Estación Villa", "Aranjuez", "Berlín", "La Piñuela", "San Isidro",
                   "Palermo", "Bermejal",
                   "San Pedro", "Sevilla", "Brasilia", "Manrique Central 1", "Manrique 1 Central 2", "Campo Valdés 1",
                   "Campo Valdés 2", "Popular 1 y 2", "Santo Domingo Savio 1", "Santo Domingo Savio 2", "Moscú 1",
                   "Moscú 2",
                   "Granizal,", "La Isla", "El Raizal", "El Playón de los Comuneros 1 (La Frontera)", "Moravia",
                   "El Jardín",
                   "Las Nieves", "María Cano", "Carambolas", "Villa Roca", "La Esperanza", "La Avanzada",
                   "El Compromiso",
                   "Carpinelo", "Versalles 1", "Versalles 2", "San José la Cima 1", "San José La Cima 2",
                   "Bello Horizonte",
                   "Oriente", "La Cruz", "Villa Guadalupe", "San Pablo", "La Francia", "Andalucía", "La Rosa",
                   "Santa Cruz",
                   "La Salle", "Las Granjas", "Manrique 1 Oriental", "El Pomar", "Las Esmeraldas", "Santa Inés",
                   "San Blas",
                   "Niza Norte (Villa Niza)"]
  Noroccidental = ["Noroccidental", "Robledo", "Cerro El Volador", "El Cucaracho", "Palenque 1 y 2", "San Germán",
                     "La Pilanca", "El Progreso",
                     "Iguaná", "Lenin", "Aures", "Mirador del 12", "Picacho", "Picachito", "Salvador", "Allende",
                     "Jorge Eliécer",
                     "Gaitán", "La Torre", "Santa Teresa de", "Jesús", "Armero II", "Búcaros", "El Paraíso",
                     "El bosque",
                     "El Triunfo",
                     "Brasil", "Los Arrayanes", "El Progreso", "La Minita", "San Nicolás", "María Auxiliadora",
                     "F.Gómez",
                     "Castilla",
                     "Caribe", "Belalcázar", "El Día", "San Martín", "La Esperanza", "Kennedy", "Castillita", "Miramar",
                     "Santa Margarita", "Alfonso López", "Pedregal", "Florencia", "Boyacá", "Las Brisas", "Antonio Zea",
                     "López de Mesa", "Córdoba", "Téjelo", "Santander", "12 de Octubre", "Tricentenario",
                     "Bello Horizonte",
                     "La Pola",
                     "Monteverde", "Villaflora", "Vallejuelos", "Villa Sofía", "Romeral", "Doña María", "Robledo",
                     "Nebraska",
                     "El Cortijo", "Candelaria"]
  Centroriental = ["Centroriental", "Guayaquil", "Colón", "Sucre", "La Ladera", "El Salvador", "Loreto",
                     "Villa Hermosa",
                     "Enciso",
                     "La Milagrosa", "Alejandro", "Echavarría", "La Mansión", "Caicedo", "La Toma", "San Diego",
                     "Las Palmas",
                     "La Independencia", "Perpetuo Socorro", "Corazón de Jesús", "Barrio Nuevo", "Llanaditas",
                     "Buenos Aires",
                     "Boston", "Prado", "Villa Nueva", "San Benito", "Candelaria", "Corazón de Jesús", "Bomboná",
                     "Los Ángeles",
                     "San Miguel", "Villatina", "Llanaditas", "Lomas de Llanaditas", "Julio Rincón", "Manuel Morales",
                     "Villa Turbay",
                     "Juan Pablo II", "San Antonio", "Las Estancias", "Santa. Lucía", "8 de Marzo", "13 de Noviembre",
                     "La Libertad",
                     "La Primavera", "El Edén", "La Sierra", "Golondrinas", "Brisas de Oriente", "El Vergel", "Enciso",
                     "Loyola",
                     "Los Cerros", "Diego Echavarría", "La Colina", "Pinar del Cerro", "Caunces de Oriente", "Cataluña",
                     "Colinas de La", "Candelaria", "Quintas de la Playa", "Urbanización Los Cerros",
                     "Urbanización El Carmelo",
                     "Urbanización La Palma", "Isaac Gaviria"]
  Centroccidental = ["Centroccidental", "El Salado", "Betania", "La Puerta", "La Loma", "El Corazón", "Belencito",
                       "El Coco", "El Socorro",
                       "Campo Alegre", "La América", "San Javier", "Floresta", "El Danubio", "Barrio Cristóbal",
                       "Lorena",
                       "Laureles",
                       "Miravalle", "Florida", "Ferrini", "La Independencia 1,", "La Independencia 2",
                       "La Independencia 3",
                       "Nuevos Conquistadores", "La Colina", "Fuente Clara", "Blanquizal", "La Quiebra",
                       "Santa Rosa de Lima",
                       "La Pradera", "Los Alcázares", "Antonio Nariño", "Metropolitano", "20 de Julio", "San Joaquín",
                       "Carlos E. Restrepo", "Santa Mónica", "Santa Lucía", "Calasanz", "Conquistadores", "Velódromo",
                       "Unidad Deportiva", "Florida Nueva", "Simón Bolívar", "Bolivariana", "Suramericana"]
  Suroriental = ["Suroriental", "Loma de los Parra", "Loma de Los González", "El Garabato", "El Tesoro",
                   "Loma de Los Mangos", "La Chacona",
                   "El Poblado", "Aguacatala", "Castropol", "Patio Bonito", "LLeras", "Santa María de los Ángeles",
                   "Villa Carlota", "Barrio Colombia", "Manila", "Astorga", "Provenza", "Alejandría", "Los Balsos",
                   "Las Lomas",
                   "Altos del Poblado", "San Lucas", "Florida", "El Castillo", "El Diamante", "Los Naranjos",
                   "El Remanso",
                   "El Futuro", "Guadalajara", "Vegas del Poblado"]
  Suroccidental = ["Suroccidental", "Cristo Rey", "Nutibara", "Barrio Antioquia", "El Rodeo", "Altavista",
                     "El Rincón",
                     "Las Mercedes", "Belén",
                     "Guayabal", "Alpinos", "Trinidad", "San Bernardo", "Las Playas", "Granada", "Betania", "Sucre",
                     "Zafra", "Apolo",
                     "Las Violetas", "Las Playas", "Rafael Uribe Uribe", "Los Libertadores", "La Castellana",
                     "Santa fe",
                     "Colina del Sur", "Coimita", "Shellmar", "Noel", "Campo Amor", "San Pablo", "Manzanares",
                     "Mallorca",
                     "Aliadas",
                     "Rosales", "Fátima", "La Nubia", "Los Alpes", "La Palma", "La Castellana", "La Mota", "El Enclave",
                     "Kalamarí",
                     "El Rodeo", "Loma de los Bernal"]
  Distrito_rural = ["Distrito rural", "Altavista", "Palmitas", "Santa Elena", "San Cristóbal", "San Antonio de Prado"]

  if barrio is not None:
    for listaActZona in [Nororiental, Noroccidental, Centroriental, Centroccidental, Suroriental, Suroccidental, Distrito_rural]:
      if barrio in listaActZona:
        zonaEncontrada = True
        zona = listaActZona[0]
        break
  return [zonaEncontrada, zona]

link_problem = {}
problematic_links = []
visited_Alnago = []


inmuebles = ['Apartaestudio', 'Apartamento', 'Bodega', 'Casa', 'Local', 'Oficina']

def get_data_tiempo(url):
    try:
        r = requests.get(url, timeout=3000, verify=False)
    except:
        sleep(60)
        try:
            r = requests.get(url, timeout=3000, verify=False)
        except:
            sleep(300)
            r = requests.get(url, timeout=3000, verify=False)

    return r.text

secciones = ['https://alnago.com/estado/venta/']

def Lista_Inmuebles_Alnago():
  server = 'https://www.alnago.com/estado/venta/'
  full_link = 'https://alnago.com/estado/venta/'
  stop = 0
  aux = 0
  acum = 2

  while acum <= 32:
  # print('While:',full_link)
    link_problem.clear()
    link_problem.setdefault(full_link, full_link)
    BS = BeautifulSoup(get_data_tiempo(full_link), "html5lib")
    Inmuebles_Alnago(BS,server)
    try:
      next_link = 'page/'+str(acum)
        
      full_link = server+next_link
      acum += 1
      print(full_link)
    except Exception as ex:
      stop = 1


def Inmuebles_Alnago(BS, server):
  inmuebles_raw = BS.find_all('a', 'listing-featured-thumb hover-effect')

  for i in inmuebles_raw:
    link_inmueble = str(i['href'])
    link_problem.clear()
    link_problem.setdefault(link_inmueble, link_inmueble)
    if (link_inmueble in visited_Alnago or link_inmueble in problematic_links):
            continue
    inmueble = BeautifulSoup(get_data_tiempo(link_inmueble), "html5lib")
    print('Link: ', link_inmueble)    





    try:
      tipo_inmueble = inmueble.find_all('li', 'breadcrumb-item')[2].find('span').text
    except Exception as ex:
        print('Except tipo_inmueble:', ex, 'Link:', link_inmueble)
        problematic_links.append(link_inmueble)
        continue

    if tipo_inmueble in inmuebles:

    
      try:
        barrio = inmueble.find_all('li', 'detail-area')[0].find('span').text
        #print(validate_zone(barrio))
      except Exception as ex:
        print('Except barrio:', ex, 'Link:', link_inmueble)
        problematic_links.append(link_inmueble)
        continue

      try:
        extraccion = validate_zone(barrio)
      except Exception as ex:
        print('Except extraccion:', ex, 'Link:', link_inmueble)
        problematic_links.append(link_inmueble)
        continue


      if extraccion[0]:
        zonaHub = extraccion[1]

        try:
          habitaciones = inmueble.find_all('div', 'fw-property-amenities-data')[1].text.split('\t')[16]
        except Exception as ex:
          print('Except habitaciones:', ex, 'Link:', link_inmueble)
          problematic_links.append(link_inmueble)
          continue  
            
        try:
          bath = inmueble.find_all('div', 'fw-property-amenities-data')[2].text.split('\t')[16]
        except Exception as ex:
          print('Except Bath:', ex, 'Link:', link_inmueble)
          problematic_links.append(link_inmueble)
          continue
        
        try:
          tam_propiedad = inmueble.find_all('div', 'fw-property-amenities-data')[3].text.split('\t')[16].split(' ')[0]
        except Exception as ex:
          print('Except tam_propiedad:', ex, 'Link:', link_inmueble)
          problematic_links.append(link_inmueble)
          continue

        try:
          descripcion = inmueble.find_all('div', 'block-content-wrap')[0].find('p').text
        except Exception as ex:
          print('Except descripcion:', ex, 'Link:', link_inmueble)
          problematic_links.append(link_inmueble)
          continue
          
        try:
          valor_inmueble = inmueble.find_all('li', 'item-price')[0].text
        except Exception as ex:
          print('Except valor_inmueble:', ex, 'Link:', link_inmueble)
          problematic_links.append(link_inmueble)
          continue
        
        

        try:
          cantidad_parqueaderos = inmueble.find_all('div', 'fw-property-amenities-data')[4].text.split('\t')
          print(cantidad_parqueaderos)

          if (cantidad_parqueaderos[0] == 'ParqueaderoPrivado' or cantidad_parqueaderos[0] == 'ParqueaderoComún'):
            cantidad_parqueaderos = 1
          elif len(cantidad_parqueaderos) > 0:
            if cantidad_parqueaderos[16] == 'Privado' or cantidad_parqueaderos[16] == 'Garaje':
              cantidad_parqueaderos = 1
            else:
              cantidad_parqueaderos = 0
          else:
            cantidad_parqueaderos = 0
        except Exception as ex:
          print('Except cantidad_parqueaderos:', ex, 'Link:', link_inmueble)
          if cantidad_parqueaderos[0] == 'ParqueaderoNinguno':
            cantidad_parqueaderos = 0
          problematic_links.append(link_inmueble)
          continue
          
          
          


        

        

        print(f"Barrio {barrio}")
        print(f"Zona {zonaHub}")
        print(f"habitaciones {habitaciones}")
        print(f"Baños {bath}")
        print(f"Tamaño Propiedad {tam_propiedad}")
        print(f"Descripcion {descripcion}")
        print(f"Tipo de inmueble {tipo_inmueble}")
        print(f"Valor inmueble {valor_inmueble}")
        print(f"Cantidad parqueaderos {cantidad_parqueaderos}")

        #print(problematic_links)   
    

if __name__ == '__main__':
    Lista_Inmuebles_Alnago()