# -*- coding: utf-8 -*-
"""emergencyScrapping.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qp3bJ-P2KUmexa-4TV7oN_df9oAbOnT5
"""

from bs4 import BeautifulSoup
import requests
import re

"""EspacioUrbano

pinta bien

Pai adelanté un roce mientras jugabas al LoL, att: el negrito de ojos claros O Z U N A
"""

Medellín_Nororiental = ["Medellín Nororiental", "El Chagualo", "Estación Villa", "Aranjuez", "Berlín", "La Piñuela", "San Isidro", "Palermo", "Bermejal",
      "San Pedro", "Sevilla", "Brasilia", "Manrique Central 1", "Manrique 1 Central 2", "Campo Valdés 1",
      "Campo Valdés 2", "Popular 1 y 2", "Santo Domingo Savio 1", "Santo Domingo Savio 2", "Moscú 1", "Moscú 2",
      "Granizal,", "La Isla", "El Raizal", "El Playón de los", "Comuneros 1 (La Frontera)", "Moravia", "El Jardín",
      "Las Nieves", "María Cano", "Carambolas", "Villa Roca", "La Esperanza", "La Avanzada", "El Compromiso",
      "Carpinelo", "Versalles 1", "Versalles 2", "San José la Cima 1", "San José La Cima 2", "Bello Horizonte",
      "Oriente", "La Cruz", "Villa Guadalupe", "San Pablo", "La Francia", "Andalucía", "La Rosa", "Santa Cruz",
      "La Salle", "Las Granjas", "Manrique 1 Oriental", "El Pomar", "Las Esmeraldas", "Santa Inés", "San Blas",
      "Niza Norte (Villa Niza)"]
Medellín_Noroccidental = ["Medellín Noroccidental", "Robledo", "Cerro El Volador", "El Cucaracho", "Palenque 1 y 2", "San Germán", "La Pilanca", "El Progreso",
      "Iguaná", "Lenin", "Aures", "Mirador del 12", "Picacho", "Picachito", "Salvador", "Allende", "Jorge Eliécer",
      "Gaitán", "La Torre", "Santa Teresa de", "Jesús", "Armero II", "Búcaros", "El Paraíso", "El bosque", "El Triunfo",
      "Brasil", "Los Arrayanes", "El Progreso", "La Minita", "San Nicolás", "María Auxiliadora", "F.Gómez", "Castilla",
      "Caribe", "Belalcázar", "El Día", "San Martín", "La Esperanza", "Kennedy", "Castillita", "Miramar",
      "Santa Margarita", "Alfonso López", "Pedregal", "Florencia", "Boyacá", "Las Brisas", "Antonio Zea",
      "López de Mesa", "Córdoba", "Téjelo", "Santander", "12 de Octubre", "Tricentenario", "Bello Horizonte", "La Pola",
      "Monteverde", "Villaflora", "Vallejuelos", "Villa Sofía", "Romeral", "Doña María", "Robledo", "Nebraska",
      "El Cortijo", "Candelaria"]
Medellín_Centroriental = ["Medellín Centroriental", "Guayaquil", "Colón", "Sucre", "La Ladera", "El Salvador", "Loreto", "Villa Hermosa", "Enciso",
      "La Milagrosa", "Alejandro", "Echavarría", "La Mansión", "Caicedo", "La Toma", "San Diego", "Las Palmas",
      "La Independencia", "Perpetuo Socorro", "Corazón de Jesús", "Barrio Nuevo", "Llanaditas", "Buenos Aires",
      "Boston", "Prado", "Villa Nueva", "San Benito", "Candelaria", "Corazón de Jesús", "Bomboná", "Los Ángeles",
      "San Miguel", "Villatina", "Llanaditas", "Lomas de Llanaditas", "Julio Rincón", "Manuel Morales", "Villa Turbay",
      "Juan Pablo II", "San Antonio", "Las Estancias", "Santa. Lucía", "8 de Marzo", "13 de Noviembre", "La Libertad",
      "La Primavera", "El Edén", "La Sierra", "Golondrinas", "Brisas de Oriente", "El Vergel", "Enciso", "Loyola",
      "Los Cerros", "Diego Echavarría", "La Colina", "Pinar del Cerro", "Caunces de Oriente", "Cataluña",
      "Colinas de La Candelaria", "Quintas de la Playa", "Urbanización Los Cerros", "Urbanización El Carmelo",
      "Urbanización La Palma", "Isaac Gaviria"]
Medellín_Centroccidental = ["Medellín Centroccidental", "El Salado", "Betania", "La Puerta", "La Loma", "El Corazón", "Belencito", "El Coco", "El Socorro",
      "Campo Alegre", "La América", "San Javier", "Floresta", "El Danubio", "Barrio Cristóbal", "Lorena", "Laureles",
      "Miravalle", "Florida", "Ferrini", "La Independencia 1,", "La Independencia 2", "La Independencia 3",
      "Nuevos Conquistadores", "La Colina", "Fuente Clara", "Blanquizal", "La Quiebra", "Santa Rosa de Lima",
      "La Pradera", "Los Alcázares", "Antonio Nariño", "Metropolitano", "20 de Julio", "San Joaquín",
      "Carlos E. Restrepo", "Santa Mónica", "Santa Lucía", "Calasanz", "Conquistadores", "Velódromo",
      "Unidad Deportiva", "Florida Nueva", "Simón Bolívar", "Bolivariana", "Suramericana"]
Medellín_Suroriental = ["Medellín Suroriental", "Loma de los Parra", "Loma de Los González", "El Garabato", "El Tesoro", "Loma de Los Mangos", "La Chacona",
      "El Poblado", "Aguacatala", "Castropol", "Patio Bonito", "LLeras", "Santa María de los Ángeles",
      "Villa Carlota", "Barrio Colombia", "Manila", "Astorga", "Provenza", "Alejandría", "Los Balsos", "Las Lomas",
      "Altos del Poblado", "San Lucas", "Florida", "El Castillo", "El Diamante", "Los Naranjos", "El Remanso",
      "El Futuro", "Guadalajara", "Vegas del Poblado"]
Medellín_Suroccidental = ["Medellín Suroccidental", "Cristo Rey", "Nutibara", "Barrio Antioquia", "El Rodeo", "Altavista", "El Rincón", "Las Mercedes", "Belén",
      "Guayabal", "Alpinos", "Trinidad", "San Bernardo", "Las Playas", "Granada", "Betania", "Sucre", "Zafra", "Apolo",
      "Las Violetas", "Las Playas", "Rafael Uribe Uribe", "Los Libertadores", "La Castellana", "Santa fe",
      "Colina del Sur", "Coimita", "Shellmar", "Noel", "Campo Amor", "San Pablo", "Manzanares", "Mallorca", "Aliadas",
      "Rosales", "Fátima", "La Nubia", "Los Alpes", "La Palma", "La Castellana", "La Mota", "El Enclave", "Kalamarí",
      "El Rodeo", "Loma de los Bernal"]
Medellín_Rural = ["Medellín Rural", "Altavista", "Palmitas", "Santa Elena", "San Cristóbal", "San Antonio de Prado"]

def zona_finder(barrio):
    for listaActZona in [Medellín_Nororiental, Medellín_Noroccidental, Medellín_Centroriental,
                                Medellín_Centroccidental, Medellín_Suroriental, Medellín_Suroccidental,
                                Medellín_Rural]:
        if barrio in listaActZona:
            return listaActZona[0]         
    return "Medellín"

def cartaProcesor(linkCarta, municipio):
  auxPet = requests.get(linkCarta, headers=headers)
  auxSoup = BeautifulSoup(auxPet.content, "html.parser")

  try:
    titulo = auxSoup.find_all("div", class_= "text-center")[1].find_all("h3")[2].text
  except:
    print("descTitulo", linkCarta)
    return None

  content_barrio = auxSoup.find("div", class_= "text-center").text
  barrio = re.search("[^/]*$", content_barrio).group(0).strip()

  try:
    tipo_inmueble = titulo.split(" ")[0]
  except:
    print("descTipo", linkCarta)
    return None

  try:
    valor_str = re.search("[^VENTA $]*$", auxSoup.find_all("div", class_= "text-center")[1].find_all("h3")[0].text.strip()).group(0)
    valor_str1 = valor_str.replace(",", "")
    valor_inmueble = int(valor_str1)
  except:
    print("descValor", linkCarta)
    return None
  
  municipio = municipio
  if municipio == "Medellín":
    municipio = zona_finder(barrio)

  try:
    habitaciones_str = auxSoup.find_all("div", class_= "text-center")[1].find("span", class_="fa fa-bed").text.strip()[0]
    cantidad_habitaciones = int(habitaciones_str)
  except:
    print("descHabi", linkCarta)
    return None 
  
  try:
    area_total = round(float(auxSoup.find("table", class_="table table-striped").find_all("tr")[2].find_all("td")[1].text.strip().split(" ")[0]), 2)
  except:
    print("descArea", linkCarta)
    return None
  
  try:
    area_construida = round(float(auxSoup.find("table", class_="table table-striped").find_all("tr")[2].find_all("td")[1].text.strip().split(" ")[0]), 2)
  except:
    area_construida = None
  
  try:
    descripcion= auxSoup.find("div", align= "justify").find("p").text.strip()
  except:
    descripcion = None 

  try:
    vendedor = auxSoup.find("div", class_="card").find("div", class_="card-body").find("p").text
  except:
    vendedor = None 
  
  try:
    cantidad_banos = int(auxSoup.find_all("div", class_= "text-center")[1].find("span", class_="fa fa-bath").text.strip()[0])
  except:
    print("descBaños", linkCarta)
    return None
  
  costo_administracion = None
  inmueble_nuevo = False
  cantidad_parqueaderos = int(auxSoup.find("table", class_="table table-striped").find_all("tr")[9].find_all("td")[1].text.strip().split(" ")[0])
  costo_servicios_publicos = None

  estrato = int(auxSoup.find("table", class_="table table-striped").find_all("tr")[1].find_all("td")[1].text.strip())
  if estrato == 0:
    estrato = None

  imagen_inmueble = "https://www.espaciourbano.com/FotosA/"+ re.search("[^xId=]*$", linkCarta).group(0).strip() +"_1.jpg"
  imgPet = requests.get(imagen_inmueble, headers=headers).status_code
  if imgPet != 200:
    print(imgPet)
    print("descimg", linkCarta)
    return None

  return {
        "nombre_fuente": "espaciourbano.com",
        "nombre_publicacion": titulo,
        "url_fuente": linkCarta,
        "tipo_inmueble": tipo_inmueble,
        "valor_inmueble": valor_inmueble,
        "municipio": municipio,
        "barrio": barrio,
        "cantidad_habitaciones": cantidad_habitaciones,
        "area_total": area_total,
        "area_construida": area_construida,
        "descripcion": descripcion,
        "vendedor": vendedor,
        "cantidad_banos": cantidad_banos,
        "costo_administracion": costo_administracion,
        "cantidad_parqueaderos": cantidad_parqueaderos,
        "costo_servicios_publicos": costo_servicios_publicos,
        "estrato": estrato,
        "inmueble_nuevo": inmueble_nuevo,
        "imagen_inmueble": imagen_inmueble
    }




headers = {"User-agent": "Mozilla/5.0"}
linkBaseCarta = "https://www.espaciourbano.com/BR_fichaDetalle_Vivienda.asp?xId="
tipos = ["1","2"] #Apartamentos y casas, respectivamente
ciudades = {"10000": "Medellín", #medellin-centro, 
            "10027": "Medellín", #medellin-elpoblado
            "10028": "Medellín", #medellin-laureles
            "10029": "Medellín", #medellin-belen
            "10006": "Caldas",
            "10032": "Barbosa",
            "10008": "Copacabana",
            "10031": "Girardota",
            "10007": "Bello",
            "10002": "Itagüí",
            "10001": "Envigado",
            "10005": "Sabaneta",
            "10003": "La Estrella"
            } 

ultimaCarta = "Esto solo inicializa ultimaCarta, y sirve para averiguar si ya no hay más paginas para el tipo y ciudad actual"


for tipoActual in tipos:
  for ciudadActual in ciudades.keys():
    offset = 0
    linkBase = "https://www.espaciourbano.com/BR_Buscaranuncios_Resultado.asp?sZona="+ tipoActual +"&sCiudad="+ ciudadActual +"&sRango1=&sRango2=&offset="
    while 1:
      linkPagina = linkBase + str(offset)
      peticion = requests.get(linkPagina, headers=headers)
      soup = BeautifulSoup(peticion.content, "html.parser")
      listaInmuebles = soup.find_all("table", class_="Destacado")
      listaCartas = [linkBaseCarta+s.find("a")["href"].split("=")[1] for s in listaInmuebles]

      print("informacion actual:","pagina=", (offset/20)+1,"Ciudad Actual=",ciudadActual,"Tipo Actual=",tipoActual)
      if listaCartas[-1] == ultimaCarta:
        print("Ya no hay mas paginas para este tipo y ciudad, siguiente")
        break
      else:
        ultimaCarta = listaCartas[-1]
      offset += 20
      for i in listaCartas:
        inmuebleActual = cartaProcesor(i,ciudades[ciudadActual])
        #Si el inmuebleActual es de valor None, se descarta el inmueble (Ya que la función cartaProcesor puede retornar None)
        print(inmuebleActual)

imagen_inmueble1 = "https://www.espaciourbano.com/FotosA/1122687_1.jpg"
imagen_inmueble2 = "https://www.espaciourbano.com/FotosA/12268_1.jpg"
imgPet = requests.get(imagen_inmueble1, headers=headers).status_code
imgpet2 = requests.get(imagen_inmueble2, headers=headers).status_code
print(imgPet, imgpet2)