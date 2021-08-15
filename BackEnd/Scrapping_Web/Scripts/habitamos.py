from bs4 import BeautifulSoup
import requests
import re

def extraccion_barrio(barrio):
    Medellín_Nororiental = ["Medellín Nororiental", "El Chagualo", "Estación Villa", "Aranjuez", "Berlín", "La Piñuela",
                            "San Isidro", "Palermo", "Bermejal",
                            "San Pedro", "Sevilla", "Brasilia", "Manrique Central 1", "Manrique 1 Central 2",
                            "Campo Valdés 1",
                            "Campo Valdés 2", "Popular 1 y 2", "Santo Domingo Savio 1", "Santo Domingo Savio 2",
                            "Moscú 1", "Moscú 2",
                            "Granizal,", "La Isla", "El Raizal", "El Playón de los", "Comuneros 1 (La Frontera)",
                            "Moravia", "El Jardín",
                            "Las Nieves", "María Cano", "Carambolas", "Villa Roca", "La Esperanza", "La Avanzada",
                            "El Compromiso",
                            "Carpinelo", "Versalles 1", "Versalles 2", "San José la Cima 1", "San José La Cima 2",
                            "Bello Horizonte",
                            "Oriente", "La Cruz", "Villa Guadalupe", "San Pablo", "La Francia", "Andalucía", "La Rosa",
                            "Santa Cruz",
                            "La Salle", "Las Granjas", "Manrique 1 Oriental", "El Pomar", "Las Esmeraldas",
                            "Santa Inés", "San Blas",
                            "Niza Norte (Villa Niza)", "Manrique", "Popular", "Campo Valdés N° 1"]
    Medellín_Noroccidental = ["Medellín Noroccidental", "Robledo", "Cerro El Volador", "El Cucaracho", "Palenque 1 y 2",
                              "San Germán", "La Pilanca", "El Progreso",
                              "Iguaná", "Lenin", "Aures", "Mirador del 12", "Picacho", "Picachito", "Salvador",
                              "Allende", "Jorge Eliécer",
                              "Gaitán", "La Torre", "Santa Teresa de", "Jesús", "Armero II", "Búcaros", "El Paraíso",
                              "El bosque", "El Triunfo",
                              "Brasil", "Los Arrayanes", "El Progreso", "La Minita", "San Nicolás", "María Auxiliadora",
                              "F.Gómez", "Castilla",
                              "Caribe", "Belalcázar", "El Día", "San Martín", "La Esperanza", "Kennedy", "Castillita",
                              "Miramar",
                              "Santa Margarita", "Alfonso López", "Pedregal", "Florencia", "Boyacá", "Las Brisas",
                              "Antonio Zea",
                              "López de Mesa", "Córdoba", "Téjelo", "Santander", "12 de Octubre", "Tricentenario",
                              "Bello Horizonte", "La Pola",
                              "Monteverde", "Villaflora", "Vallejuelos", "Villa Sofía", "Romeral", "Doña María",
                              "Robledo", "Nebraska",
                              "El Cortijo", "Candelaria", "Doce de Octubre", "La Pilarica", "Doce de Octubre Nº 1"]
    Medellín_Centroriental = ["Medellín Centroriental", "Guayaquil", "Colón", "Sucre", "La Ladera", "El Salvador",
                              "Loreto", "Villa Hermosa", "Enciso",
                              "La Milagrosa", "Alejandro", "Echavarría", "La Mansión", "Caicedo", "La Toma",
                              "San Diego", "Las Palmas",
                              "La Independencia", "Perpetuo Socorro", "Corazón de Jesús", "Barrio Nuevo", "Llanaditas",
                              "Buenos Aires",
                              "Boston", "Prado", "Villa Nueva", "San Benito", "Candelaria", "Corazón de Jesús",
                              "Bomboná", "Los Ángeles",
                              "San Miguel", "Villatina", "Llanaditas", "Lomas de Llanaditas", "Julio Rincón",
                              "Manuel Morales", "Villa Turbay",
                              "Juan Pablo II", "San Antonio", "Las Estancias", "Santa. Lucía", "8 de Marzo",
                              "13 de Noviembre", "La Libertad",
                              "La Primavera", "El Edén", "La Sierra", "Golondrinas", "Brisas de Oriente", "El Vergel",
                              "Enciso", "Loyola",
                              "Los Cerros", "Diego Echavarría", "La Colina", "Pinar del Cerro", "Caunces de Oriente",
                              "Cataluña",
                              "Colinas de La Candelaria", "Quintas de la Playa", "Urbanización Los Cerros",
                              "Urbanización El Carmelo",
                              "Urbanización La Palma", "Isaac Gaviria", "Nogal", "Bomboná Nº 1", "Bombona Nº 2",
                              "La Candelaria", "Los Angeles"]
    Medellín_Centroccidental = ["Medellín Centroccidental", "El Salado", "Betania", "La Puerta", "La Loma",
                                "El Corazón", "Belencito", "El Coco", "El Socorro",
                                "Campo Alegre", "La América", "San Javier", "Floresta", "El Danubio",
                                "Barrio Cristóbal", "Lorena", "Laureles",
                                "Miravalle", "Florida", "Ferrini", "La Independencia 1,", "La Independencia 2",
                                "La Independencia 3",
                                "Nuevos Conquistadores", "La Colina", "Fuente Clara", "Blanquizal", "La Quiebra",
                                "Santa Rosa de Lima",
                                "La Pradera", "Los Alcázares", "Antonio Nariño", "Metropolitano", "20 de Julio",
                                "San Joaquín",
                                "Carlos E. Restrepo", "Santa Mónica", "Santa Lucía", "Calasanz", "Conquistadores",
                                "Velódromo",
                                "Unidad Deportiva", "Florida Nueva", "Simón Bolívar", "Bolivariana", "Suramericana",
                                "Estadio", "Los Colores", "Almería", "Las Acacias", "Girardot", "Calasanz Parte Alta",
                                "Cuarta Brigada", "San Javier Nº 2", "Naranjal"]
    Medellín_Suroriental = ["Medellín Suroriental", "Loma de los Parra", "Loma de Los González", "El Garabato",
                            "El Tesoro", "Loma de Los Mangos", "La Chacona",
                            "El Poblado", "Aguacatala", "Castropol", "Patio Bonito", "LLeras",
                            "Santa María de los Ángeles",
                            "Villa Carlota", "Barrio Colombia", "Manila", "Astorga", "Provenza", "Alejandría",
                            "Los Balsos", "Las Lomas",
                            "Altos del Poblado", "San Lucas", "Florida", "El Castillo", "El Diamante", "Los Naranjos",
                            "El Remanso",
                            "El Futuro", "Guadalajara", "Vegas del Poblado", "Los Balsos Nº 1", "Los Balsos Nº 2",
                            "La Calera", "El Campestre", "La Tomatera", "Ciudad del Rio", "Loma Cola del Zorro",
                            "Alto de las Palmas", "La Concha", "Las Lomas Nº 1", "Las Lomas Nº 2", "La Frontera",
                            "Santa Maria de Los Angeles", "Lalinde", "La Aguacatala", "Milla de Oro",
                            "Loma de San Julian", "Loma Los Gonzalez", "La Florida", "La Visitación", "Oviedo",
                            "El Diamante Nº 2", "Loma del Indio"]
    Medellín_Suroccidental = ["Medellín Suroccidental", "Cristo Rey", "Nutibara", "Barrio Antioquia", "El Rodeo",
                              "Altavista", "El Rincón", "Las Mercedes", "Belén",
                              "Guayabal", "Alpinos", "Trinidad", "San Bernardo", "Las Playas", "Granada", "Betania",
                              "Sucre", "Zafra", "Apolo",
                              "Las Violetas", "Las Playas", "Rafael Uribe Uribe", "Los Libertadores", "La Castellana",
                              "Santa fe",
                              "Colina del Sur", "Coimita", "Shellmar", "Noel", "Campo Amor", "San Pablo", "Manzanares",
                              "Mallorca", "Aliadas",
                              "Rosales", "Fátima", "La Nubia", "Los Alpes", "La Palma", "La Castellana", "La Mota",
                              "El Enclave", "Kalamarí",
                              "El Rodeo", "Loma de los Bernal", "Loma de Los Bernal", "Rodeo Alto", "Malibú",
                              "Los Almendros", "Alameda", "La Floresta", "Santa Teresita", "El Velódromo", "Santa Fe",
                              "Belén Rodeo Alto", "La Gloria"]
    Medellín_Rural = ["Medellín Rural", "Altavista", "Palmitas", "Santa Elena", "San Cristóbal", "San Antonio de Prado",
                      "San Cristóbal"]

    for listaActbarrio in [Medellín_Nororiental, Medellín_Noroccidental, Medellín_Centroriental, Medellín_Centroccidental, Medellín_Suroriental, Medellín_Suroccidental, Medellín_Rural]:
        if barrio in listaActbarrio:
            return True
    return False

nombre_fuente = 'https://habitamos.com.co/'
url_fuente = []
nombre_publicacion = []
descripcion = []
valor_inmueble = []
cantidad_habitaciones = []
tipo_inmueble = []
area_total = []
cantidad_banos = []
cantidad_parqueaderos = []
barrio = [] #Barrio
imagen_inmueble = []
municipio = []
area_construida = []
vendedor = []
costo_administracion = []
costo_servicios_publicos = []
estrato = []
inmueble_nuevo = []

nombre = []
info = []
info_Dir = []
ind_malos = []
barrio2 = []
imagen_inmueble2 = []
info_Dir2 = []
url_fuente2 = []

k = 1
while(True):
    page = requests.get('https://habitamos.com.co/ventas/page/' + str(k))
    soup = BeautifulSoup(page.content, 'html.parser')
    if(len(soup.find_all('a', {'class': 'hover-effect'}))==0):
        break
    for a in soup.find_all('a', {'class': 'hover-effect'}):
        url_fuente2.append(a['href'])
    k = k+1

k = 0
for i in url_fuente2:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')

    for j in soup.find_all('div', {'class': 'detail-address detail-block target-block'}):
        info_Dir2.append(j.text)

    try:
        for j in soup.find_all('div', {'class': 'item'}):
            cadena = re.search(r'(https:\/\/\w+.com.co\/\w+-content\/uploads\/\d+\/\d+\/\w+-\w+.(jpg|jpeg|png))|'
                               r'(https:\/\/\w+.com.co\/\w+-content\/uploads\/\d+\/\d+\/\w+-\w+-\w+.(jpg|jpeg|png))', str(j))
            imagen_inmueble2.append(cadena.group())
            break
    except AttributeError:
        imagen_inmueble2.append('No Especifica')
        ind_malos.append(k)

    try:
        cadena = re.search(r'Barrio: ((\w+ \w+)|(\w+))', info_Dir2[k])
        cadena = cadena.group().replace('Barrio: ', '').replace("País", '').title()
        if extraccion_barrio(cadena) == False:
            if k not in ind_malos:
                ind_malos.append(k)
        barrio2.append(cadena)
    except AttributeError:
        barrio2.append('No Especifica')
    k = k + 1

for i in range(0, len(url_fuente2)):
    if i not in ind_malos:
        barrio.append(barrio2[i])
        imagen_inmueble.append(imagen_inmueble2[i])
        info_Dir.append(info_Dir2[i])
        url_fuente.append(url_fuente2[i])

for i in url_fuente:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    municipio.append(None)
    area_construida.append(None)
    vendedor.append(None)
    costo_administracion.append(None)
    costo_servicios_publicos.append(None)
    estrato.append(None)
    inmueble_estado_uso.append(None)
    area_construida.append(0)
    vendedor.append('No especifica')
    costo_administracion.append(0)
    costo_servicios_publicos.append(0)
    estrato.append(0)
    inmueble_nuevo.append(False)
    for j in soup.find_all('div', {'class': 'table-cell'}):
        nombre.append(j.text)

    for j in soup.find_all('div', {'class': 'property-description detail-block target-block'}):
        descripcion.append(j.text)

    for j in soup.find_all('div', {'class': 'alert alert-info'}):
        info.append(j.text)

for i in range(0,len(descripcion)):
    descripcion[i] = descripcion[i].replace('\n\nDescripción\n\n', '')

for i in range(0,len(nombre)):
    if(i%2 == 0):
        nombre_publicacion.append(nombre[i])

for i in range(0,len(info)):
    try:
        cadena = re.search(r'Precio: (\$\d+,\d+,\d+,\d+)|(\$\d+,\d+,\d+)',info[i])
        cadena = cadena.group().replace('$','').replace(',','')
        valor_inmueble.append(int(cadena))
    except AttributeError:
        valor_inmueble.append(int(0))

    try:
        cadena = re.search(r'Habitaciones: (\d+)',info[i])
        cadena = cadena.group().replace('Habitaciones: ','')
        cantidad_habitaciones.append(int(cadena))
    except AttributeError:
        cantidad_habitaciones.append(int(0))

    try:
        cadena = re.search(r'Tamaño de propiedad: (\d+)', info[i])
        cadena = cadena.group().replace('Tamaño de propiedad: ','')
        area_total.append(int(cadena))
    except AttributeError:
        area_total.append(int(0))

    try:
        cadena = re.search(r'Baños: (\d+)', info[i])
        cadena = cadena.group().replace('Baños: ', '')
        cantidad_banos.append(int(cadena))
    except AttributeError:
        cantidad_banos.append(int(0))

    try:
        cadena = re.search(r'Garaje: (\d+)', info[i])
        cadena = cadena.group()
        cadena = cadena.replace('Garaje: ', '')
        cantidad_parqueaderos.append(int(cadena))
    except AttributeError:
        cantidad_parqueaderos.append(int(0))

    try:
        cadena = re.search(r'Tipo de propiedad: (\w+)', info[i])
        cadena = cadena.group().replace('Tipo de propiedad: ', '').replace('Estado', '')
        tipo_inmueble.append(cadena)
    except AttributeError:
        tipo_inmueble.append('**NO ESPECIFICA**')

    try:
        cadena = re.search(r'Ciudad: ((\w+ \w+)|(\w+))', info_Dir[i])
        cadena = cadena.group().replace('Ciudad: ', '').replace('Estado', '').title()
        if cadena == 'Medellin':
            municipio.append(cadena.replace('i','í'))
        else:
            municipio.append(cadena)
    except AttributeError:
        municipio.append('NO ESPECIFICA')

print(len(municipio))
print(len(url_fuente))