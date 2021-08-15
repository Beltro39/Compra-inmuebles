from bs4 import BeautifulSoup
import requests
import re

def extraccion_zona(barrio):
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

    if barrio is not None:
        zonaEncontrada = 0
        for listaActZona in [Medellín_Nororiental, Medellín_Noroccidental, Medellín_Centroriental, Medellín_Centroccidental, Medellín_Suroriental, Medellín_Suroccidental,Medellín_Rural]:
            if barrio in listaActZona:
                return (listaActZona[0])
                break

nombre_fuente = []
nombre_publicacion = []
valor_inmueble = []
municipio = []
vendedor = []
url_fuente = []
url_mom = []
tipo_inmueble = []
cantidad_habitaciones = []
cantidad_banos = []
cantidad_parqueaderos = []
inmueble_nuevo = []
area_total = []
area_construida = []
imagen_inmueble = []
barrio = []
estrato = []
costo_servicios_publicos = []

for i in range (1,400):

    url = 'https://www.properati.com.co/s/medellin-antioquia/venta?page=' + str(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find_all('h2', class_='StyledTitle-n9541a-4 bwJAej')
    price = soup.find_all('span', class_='StyledPrice-sc-1wixp9h-0 bZCCaW')
    barrios = soup.find_all('span', class_='StyledLocation-n9541a-7 fqaBNm')
    seller = soup.find_all('span', class_='seller-name')
    habitacionArea = soup.find_all('div', class_='StyledInfoIcons-n9541a-9 fgcFIO')
    vinculos = soup.find_all('a')

    # Verifica si llegó al final
    if (len(name) == 0):
        print('ha llegado al final')
        print(len(nombre_publicacion))
        print(len(valor_inmueble))
        print(len(barrio))
        print(len(url_fuente))
        print(len(cantidad_habitaciones))
        print(len(cantidad_banos))
        print(len(cantidad_parqueaderos))
        print(len(area_total))
        print(len(area_construida))
        print(len(tipo_inmueble))
        print(len(inmueble_nuevo))
        print(len(vendedor))
        print(len(imagen_inmueble))
        print(len(municipio))
        print(len(nombre_fuente))
        break
    else:
        print('Pagina Externa: ' + url)

    # Filtra los que no tengan precio
    try:
        if (len(price) == 0):
            continue
    except AttributeError:
        continue

    # Recorre el link inicial y aplica regex para obtener las habitaciones y las áreas

    if (len(habitacionArea) != 30):
        continue

    for i in habitacionArea:
        textoCompleto = i.text
        habitaciones = re.search(r"\d+ habitaciones",textoCompleto)
        areaTot = re.search(r"\d+ m²",textoCompleto)
        areaConstr = re.search(r"\d+ /",textoCompleto)

        if (areaTot == None or areaTot == ''):
            area_total.append(0)
        else:
            try:
                areaTot = areaTot.group()
                areaTot = areaTot.replace('m²', '')
                area_total.append(float(areaTot))
            except AttributeError:
                area_total.append(0)


        if (habitaciones == None or habitaciones == ''):
            cantidad_habitaciones.append(4)
        else:
            try:
                habitaciones = habitaciones.group()
                habitaciones = habitaciones.replace(' habitaciones', '')
                cantidad_habitaciones.append(int(habitaciones))
            except AttributeError:
                cantidad_habitaciones.append(4)


        if (areaConstr == None or areaConstr == ''):
            area_construida.append(0)
        else:
            try:
                areaConstr = areaConstr.group()
                areaConstr = areaConstr.replace(' /', '')
                area_construida.append(float(areaConstr))
            except AttributeError:
                area_construida.append(0)

    linksIni = []
    linksFin = []

# Recorre todos los links de la página
    for link in vinculos:
        cadaLink = link.get('href')
        #Verifica que contenga la estructura de los links que necesito
        if (str(cadaLink).__contains__('/detalle/')):
            linksIni.append(cadaLink)

# Recorre todos los links (duplicados) y elimina la duplicación
    for i in range (len(linksIni)):
        if (i % 2 == 0):
            linksFin.append(linksIni[i])

# Recorre los nombres y aplica regex para obtener el tipo del inmueble
    for i in name:
        nombre_publicacion.append(i.text)
        nombre_fuente.append('Properati')
        costo_servicios_publicos.append(0)
        estrato.append(0)

    for i in name:
        tipo = re.search(r"Apartamento|Casa|Finca|Local|Edificio|Lote|Oficina\WConsultorio",i.text)
        try:
            tipo = tipo.group()
            tipo_inmueble.append(tipo)
            inmueble_nuevo.append(False)
        except AttributeError:
            tipo_inmueble.append("Proyecto de Vivienda")
            inmueble_nuevo.append(True)

# Recorre los nombres y aplica regex para obtener el barrio del inmueble
    for i in name:
        zonita = re.search(r"en \D+",i.text)
        try:
            zonita = zonita.group()
            zonita = zonita.replace("en ", "")
            barrio.append(zonita)
            municipio.append(extraccion_zona(zonita))

        except AttributeError:
            barrio.append('Medellín')

    for i in price:
        i = str (i.text).replace('.','').replace('$','').replace(' ','')
        valor_inmueble.append(int (i))

    for i in seller:
        vendedor.append(i.text)

    for i in linksFin:
        url_fuente.append(i)
        url_mom.append(i)

# Recorre la página interna de cada inmueble para extraer baños, habitaciones e imagen
    for i in url_mom:
        urlInterna = i
        page = requests.get("https://www.properati.com.co" + urlInterna)
        soup2 = BeautifulSoup(page.content, 'html.parser')
        caracteristicas = soup2.find_all('div', class_='StyledTabs-sc-7zq0tq-0 dCNQdg')
        imagen = soup2.find_all('img')

        print('Link Interno: ' + "https://www.properati.com.co" + urlInterna)


        for image in imagen:
            imagen_inmueble.append(image['src'])
            break

        for i in caracteristicas:
            descripcion = i.text
            baños = re.search(r"Baños: \d+",descripcion)
            parqueaderos = re.search(r"Parqueaderos|Parqueadero", descripcion)

            if (baños == 'None' or baños == ''):
                cantidad_banos.append(2)
            else:
                try:
                    baños = baños.group().replace("Baños: ", "")
                    cantidad_banos.append(int(baños))
                except AttributeError:
                    cantidad_banos.append(2)

            if (parqueaderos == 'None' or parqueaderos == ''):
                cantidad_parqueaderos.append(0)
            else:
                try:
                    parqueaderos = parqueaderos.group()
                    cantidad_parqueaderos.append(1)
                except AttributeError:
                    cantidad_parqueaderos.append(0)

            break

    # Se reinician los links internos, ya que cambian para cada página
    url_mom.clear()



