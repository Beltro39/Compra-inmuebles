# Guía scrapping
from time import time, sleep
import datetime
import urllib.request
import json
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

link_problem = {}
problematic_links = []
visited_Espacio_Urbano = []
lista_inmuebles = []
barrios_diferentes = {}

def get_data_tiempo(url):
    try:
        r = requests.get(url, timeout=3000, verify=False)
    except:
        # print('Waiting...', datetime.datetime.now())
        sleep(60)
        # print('Waiting...', datetime.datetime.now())
        try:
            r = requests.get(url, timeout=3000, verify=False)
        except:
            # print('Waiting 2...', datetime.datetime.now())
            sleep(300)
            # print('Waiting 2...', datetime.datetime.now())
            r = requests.get(url, timeout=3000, verify=False)

    return r.text


# El siguiente metodo obtiene la lista de los resultados de la busqueda y sigue iterando sobre las paginas de los resultados de esta busqueda
# luego envía estos resultados al siguiente metodo
# https://www.espaciourbano.com/Apartamentos_Venta_Zona1.asp?idciudad=10000&Ciudad=Medell%EDn%20Zona%201%20-%20Centro
secciones = ['https://www.espaciourbano.com/Apartamentos_Venta_Zona1.asp', 'https://www.espaciourbano.com/Apartamentos_Venta_Zona2.asp', 'https://www.espaciourbano.com/Apartamentos_Venta_Zona3.asp', 'https://www.espaciourbano.com/Apartamentos_Venta_Zona4.asp', 'https://www.espaciourbano.com/Apartamentos_venta_Sabaneta.asp', 'https://www.espaciourbano.com/Apartamentos_venta_Envigado.asp',
             'https://www.espaciourbano.com/Apartamentos_Venta_Laestrella.asp', 'https://www.espaciourbano.com/Apartamentos_venta_itagui.asp', 'https://www.espaciourbano.com/Apartamentos_venta_Bello.asp', 'https://www.espaciourbano.com/comercio/ventas.asp', 'https://www.espaciourbano.com/Lotes_Venta.asp', 'https://www.espaciourbano.com/Fincas_venta.asp', 'https://www.espaciourbano.com/Agroindustriales_venta.asp', ]


def Lista_Inmuebles_Espacio_Urbano():
    server = 'https://www.espaciourbano.com/'
    for link in secciones:
        # print('for:',link)
        full_link = link
        stop = 0
        aux = 0
        while stop == 0:
            # print('While:',full_link)
            link_problem.clear()
            link_problem.setdefault(full_link, full_link)
            BS = BeautifulSoup(get_data_tiempo(full_link), "html5lib")
            Inmuebles_Espacio_Urbano(BS, server)
            try:
                next_link = BS.find('span', {'class': 'style100'}).find(
                    'span', {'class': 'style63 style62 style100 style73'}).find_all('a')
                # print(next_link)
                # print(next_link[aux]['href'])
                if aux == len(next_link):
                    continue
                else:
                    aux += 1
                full_link = server+next_link[aux]['href']
            except Exception as ex:
                stop = 1

    print('Tamaño lista:',len(lista_inmuebles))
    print(lista_inmuebles)
    print('Barrios diferentes:',barrios_diferentes)
    print('Problematic links:',problematic_links)

# En el siguiente metodo buscamos como tal los links en cada pagina que se recibe
# luego ingresamos a estos links y obtenemos la información como tal que buscamos


def Inmuebles_Espacio_Urbano(BS, server):
    inmuebles_raw = BS.find_all('table', {'class': 'Destacado'})
    # print('Inmuebles:',len(inmuebles_raw))
    nombre_fuente = 'https://www.espaciourbano.com/'
    for i in inmuebles_raw:
        # start = datetime.datetime.now()
        link_inmueble = server+str(i.a['href'])
        link_problem.clear()
        link_problem.setdefault(link_inmueble, link_inmueble)

        inmueble = BeautifulSoup(get_data_tiempo(link_inmueble), "html5lib")

        try:
            center_info = inmueble.find_all(
                'div', {'class': 'text-center'})[1].find_all('h3')
        except Exception as ex:
            print('Except center_info:', ex, 'Link:', link_inmueble)
            problematic_links.append([link_inmueble, ex])
            continue
        nombre_publicacion = center_info[2].text.upper()
        # print('Nombre de la publicación:', nombre_publicacion)
        url_fuente = link_inmueble
        # print('Enlace a la publicación:', url_fuente)
        tipo_inmueble = center_info[2].text.split(' ')[0].upper()
        # pueden salir en venta y en arriendo.....
        print('Tipo de inmueble:', tipo_inmueble)
        valor_inmueble = center_info[0].text.split('VENTA $')[1].replace(',', '')
        print('Precio:', valor_inmueble)

        try:
            features = inmueble.find(
                'table', {'class': 'table table-striped'}).find_all('tr')
        except Exception as ex:
            print('Except featuyres:', ex, 'Link:', link_inmueble)
            problematic_links.append([link_inmueble, ex])
            continue
        # print('Caracteristicas:', features)

        municipio = features[0].find_all('td')[1].text.split(' ')[0].upper()
        
        try:
            upper_info = inmueble.find_all(
                'div', {'class': 'text-center'})[0].find_all('p')
        except Exception as ex:
            print('Except upper_info:', ex, 'Link:', link_inmueble)
            problematic_links.append([link_inmueble, ex])
            continue

        barrio = upper_info[0].find('small').text.replace(' / ', '')

        if municipio == 'MEDELLIN':
            municipio = 'MEDELLÍN'
            print('Municipio:', municipio)
            aux_barrio = extraccion_zona(barrio)
            if aux_barrio != True:
                print(aux_barrio)
                barrios_diferentes.setdefault(barrio,aux_barrio)
                continue
                
        barrio = barrio.upper()
        print('Barrio:',barrio)

        cantidad_habitaciones = center_info[1].find(
            'span', {'class': 'fa fa-bed'}).text.split('+')[0]
        # int(features[5].find_all('td')[1].text))
        print('Habitaciones:', int(cantidad_habitaciones))
        area_total = round(float(features[2].find_all('td')[
                           1].text.split(' M2.')[0].replace(',','')), 2)
        print('Área total:', area_total)
        try:
            area_construida = round(
                float(features[3].find_all('td')[1].text.split(' M2.')[0]), 2)
            print('Área construida:', area_construida)
        except Exception as ex:
            print('Except area construida:', ex, 'Link:', link_inmueble)
            problematic_links.append([link_inmueble, ex])
            continue

        try:
            description = inmueble.find('div', {'align': 'justify'})
        except Exception as ex:
            print('Except description:', ex, 'Link:', link_inmueble)
            problematic_links.append([link_inmueble, ex])
            continue
        descripcion = description.text.upper()
        # print('Descripción:', descripcion)

        try:
            seller = inmueble.find_all(
                'div', {'class': 'col-sm-5'})[0].find('div', {'class': 'card-body'})
        except Exception as ex:
            print('Except seller:', ex, 'Link:', link_inmueble)
            problematic_links.append([link_inmueble, ex])
            continue
        aux_seller = str(seller.find('h4', {'class': 'card-title'}).text)+' '+str(
            seller.find('p', {'class': 'card-text'}).text)
        vendedor = aux_seller.upper()
        print('Nombre Vendedor o Agencia:', vendedor)

        cantidad_banos = int(center_info[1].find(
            'span', {'class': 'fa fa-bath'}).text.split('+')[0])
        # print('Baños:', cantidad_banos)

        costo_administracion = 0
        # print('Administración:', costo_administracion)

        cantidad_parqueaderos = int(
            features[9].find_all('td')[1].text.split(' ')[0])
        # print('Parqueaderos:', cantidad_parqueaderos)

        costo_servicios_publicos = 0
        # print('Servicios:', costo_servicios_publicos)

        estrato = int(features[1].find_all('td')[1].text)
        # print('Estrato:', estrato)

        inmueble_nuevo = False
        # print('Nuevo/Usado:', inmueble_nuevo)

        try:
            aux_imagen_inmueble = inmueble.find(
                'div', {'class': 'carousel-inner'}).find_all('div', {'class': 'carousel-item'})
            imagen_inmueble = nombre_fuente+aux_imagen_inmueble[0].img['src']
            print('Imagen:', imagen_inmueble)
        except Exception as ex:
            problematic_links.append([link_inmueble, ex])
            continue
            

        aux_inmueble = (nombre_fuente, nombre_publicacion, url_fuente, tipo_inmueble, valor_inmueble, municipio, barrio, cantidad_habitaciones, area_total, area_construida,
                        descripcion, vendedor, cantidad_banos, costo_administracion, cantidad_parqueaderos, costo_servicios_publicos, estrato, inmueble_nuevo, imagen_inmueble)
        
        lista_inmuebles.append(aux_inmueble)



# 'none'
# 0
# 'false' true nuevo


def extraccion_zona(barrio):
    barriosSinZona = []

    Medellín_Nororiental = ["Medellín Nororiental", "El Chagualo", "Estación Villa", "Aranjuez", "Berlín", "La Piñuela", "San Isidro", "Palermo", "Bermejal",
                            "San Pedro", "Sevilla", "Brasilia", "Manrique Central 1", "Manrique 1 Central 2", "Campo Valdés 1",
                            "Campo Valdés 2", "Popular 1 y 2", "Santo Domingo Savio 1", "Santo Domingo Savio 2", "Moscú 1", "Moscú 2",
                            "Granizal,", "La Isla", "El Raizal", "El Playón de los", "Comuneros 1 (La Frontera)", "Moravia", "El Jardín",
                            "Las Nieves", "María Cano", "Carambolas", "Villa Roca", "La Esperanza", "La Avanzada", "El Compromiso",
                            "Carpinelo", "Versalles 1", "Versalles 2", "San José la Cima 1", "San José La Cima 2", "Bello Horizonte",
                            "Oriente", "La Cruz", "Villa Guadalupe", "San Pablo", "La Francia", "Andalucía", "La Rosa", "Santa Cruz",
                            "La Salle", "Las Granjas", "Manrique 1 Oriental", "El Pomar", "Las Esmeraldas", "Santa Inés", "San Blas",
                            "Niza Norte (Villa Niza)", "Manrique", "Popular", "Campo Valdés N° 1","Campo Valdes","Andalucia"]
    Medellín_Noroccidental = ["Medellín Noroccidental", "Robledo", "Cerro El Volador", "El Cucaracho", "Palenque 1 y 2", "San Germán", "La Pilanca", "El Progreso",
                              "Iguaná", "Lenin", "Aures", "Mirador del 12", "Picacho", "Picachito", "Salvador", "Allende", "Jorge Eliécer",
                              "Gaitán", "La Torre", "Santa Teresa de", "Jesús", "Armero II", "Búcaros", "El Paraíso", "El bosque", "El Triunfo",
                              "Brasil", "Los Arrayanes", "El Progreso", "La Minita", "San Nicolás", "María Auxiliadora", "F.Gómez", "Castilla",
                              "Caribe", "Belalcázar", "El Día", "San Martín", "La Esperanza", "Kennedy", "Castillita", "Miramar",
                              "Santa Margarita", "Alfonso López", "Pedregal", "Florencia", "Boyacá", "Las Brisas", "Antonio Zea",
                              "López de Mesa", "Córdoba", "Téjelo", "Santander", "12 de Octubre", "Tricentenario", "Bello Horizonte", "La Pola",
                              "Monteverde", "Villaflora", "Vallejuelos", "Villa Sofía", "Romeral", "Doña María", "Robledo", "Nebraska",
                              "El Cortijo", "Candelaria", "Doce de Octubre", "La Pilarica", "Doce de Octubre Nº 1","Francisco Antonio Zea","Alfonso Lopez","Robledo ","Robledo Aures","Lopez de Mesa","Pilarica","San German"]
    Medellín_Centroriental = ["Medellín Centroriental", "Guayaquil", "Colón", "Sucre", "La Ladera", "El Salvador", "Loreto", "Villa Hermosa", "Enciso",
                              "La Milagrosa", "Alejandro", "Echavarría", "La Mansión", "Caicedo", "La Toma", "San Diego", "Las Palmas",
                              "La Independencia", "Perpetuo Socorro", "Corazón de Jesús", "Barrio Nuevo", "Llanaditas", "Buenos Aires",
                              "Boston", "Prado", "Villa Nueva", "San Benito", "Candelaria", "Corazón de Jesús", "Bomboná", "Los Ángeles",
                              "San Miguel", "Villatina", "Llanaditas", "Lomas de Llanaditas", "Julio Rincón", "Manuel Morales", "Villa Turbay",
                              "Juan Pablo II", "San Antonio", "Las Estancias", "Santa. Lucía", "8 de Marzo", "13 de Noviembre", "La Libertad",
                              "La Primavera", "El Edén", "La Sierra", "Golondrinas", "Brisas de Oriente", "El Vergel", "Enciso", "Loyola",
                              "Los Cerros", "Diego Echavarría", "La Colina", "Pinar del Cerro", "Caunces de Oriente", "Cataluña",
                              "Colinas de La Candelaria", "Quintas de la Playa", "Urbanización Los Cerros", "Urbanización El Carmelo",
                              "Urbanización La Palma", "Isaac Gaviria", "Nogal", "Bomboná Nº 1", "Bombona Nº 2", "La Candelaria", "Los Angeles","Encizo","Bombona","Caunces Oriente","Villanueva",]
    Medellín_Centroccidental = ["Medellín Centroccidental", "El Salado", "Betania", "La Puerta", "La Loma", "El Corazón", "Belencito", "El Coco", "El Socorro",
                                "Campo Alegre", "La América", "San Javier", "Floresta", "El Danubio", "Barrio Cristóbal", "Lorena", "Laureles",
                                "Miravalle", "Florida", "Ferrini", "La Independencia 1,", "La Independencia 2", "La Independencia 3",
                                "Nuevos Conquistadores", "La Colina", "Fuente Clara", "Blanquizal", "La Quiebra", "Santa Rosa de Lima",
                                "La Pradera", "Los Alcázares", "Antonio Nariño", "Metropolitano", "20 de Julio", "San Joaquín",
                                "Carlos E. Restrepo", "Santa Mónica", "Santa Lucía", "Calasanz", "Conquistadores", "Velódromo",
                                "Unidad Deportiva", "Florida Nueva", "Simón Bolívar", "Bolivariana", "Suramericana", "Estadio", "Los Colores", "Almería", "Las Acacias", "Girardot", "Calasanz Parte Alta", "Cuarta Brigada", "San Javier Nº 2", "Naranjal","Almeria","Simón Bolivar","Velodromo","Carlos E Restrepo","Laureles, las acacias","laureles"]
    Medellín_Suroriental = ["Medellín Suroriental", "Loma de los Parra", "Loma de Los González", "El Garabato", "El Tesoro", "Loma de Los Mangos", "La Chacona",
                            "El Poblado", "Aguacatala", "Castropol", "Patio Bonito", "LLeras", "Santa María de los Ángeles",
                            "Villa Carlota", "Barrio Colombia", "Manila", "Astorga", "Provenza", "Alejandría", "Los Balsos", "Las Lomas",
                            "Altos del Poblado", "San Lucas", "Florida", "El Castillo", "El Diamante", "Los Naranjos", "El Remanso",
                            "El Futuro", "Guadalajara", "Vegas del Poblado", "Los Balsos Nº 1", "Los Balsos Nº 2", "La Calera", "El Campestre", "La Tomatera", "Ciudad del Rio", "Loma Cola del Zorro", "Alto de las Palmas", "La Concha", "Las Lomas Nº 1", "Las Lomas Nº 2", "La Frontera", "Santa Maria de Los Angeles", "Lalinde", "La Aguacatala", "Milla de Oro", "Loma de San Julian", "Loma Los Gonzalez", "La Florida", "La Visitación", "Oviedo", "El Diamante Nº 2", "Loma del Indio","La Linde","Santa Ma. los Angeles","Cola del Zorro","Los Parra","Poblado","La Cola Del Zorro","Loma de Los Parra"]
    Medellín_Suroccidental = ["Medellín Suroccidental", "Cristo Rey", "Nutibara", "Barrio Antioquia", "El Rodeo", "Altavista", "El Rincón", "Las Mercedes", "Belén",
                              "Guayabal", "Alpinos", "Trinidad", "San Bernardo", "Las Playas", "Granada", "Betania", "Sucre", "Zafra", "Apolo",
                              "Las Violetas", "Las Playas", "Rafael Uribe Uribe", "Los Libertadores", "La Castellana", "Santa fe",
                              "Colina del Sur", "Coimita", "Shellmar", "Noel", "Campo Amor", "San Pablo", "Manzanares", "Mallorca", "Aliadas",
                              "Rosales", "Fátima", "La Nubia", "Los Alpes", "La Palma", "La Castellana", "La Mota", "El Enclave", "Kalamarí",
                              "El Rodeo", "Loma de los Bernal", "Loma de Los Bernal", "Rodeo Alto", "Malibú", "Los Almendros", "Alameda", "La Floresta", "Santa Teresita", "El Velódromo", "Santa Fe", "Belén Rodeo Alto", "La Gloria"," Nutibara","Belén La Palma"]
    Medellín_Rural = ["Medellín Rural", "Altavista", "Palmitas",
                      "Santa Elena", "San Cristóbal", "San Antonio de Prado", "San Cristóbal"]

    if barrio is not None:
        zonaEncontrada = 0
        for listaActZona in [Medellín_Nororiental, Medellín_Noroccidental, Medellín_Centroriental, Medellín_Centroccidental, Medellín_Suroriental, Medellín_Suroccidental,
                             Medellín_Rural]:
            if barrio in listaActZona:
                #zona = listaActZona[0] #
                zonaEncontrada = 1
                return True
        if not zonaEncontrada and not barrio in barriosSinZona:
            barriosSinZona.append(barrio)

    return barriosSinZona


if __name__ == '__main__':
    Lista_Inmuebles_Espacio_Urbano()
