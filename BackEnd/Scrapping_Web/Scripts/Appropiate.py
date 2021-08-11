"""v4:
    - Algunos tipos de inmuebles no comprendidos, comentarios añadidos en su respectivo lugar
        """

from bs4 import BeautifulSoup
import requests


def cartaPorcesador(sopa, linkCarta, municipioCarta, costo_administracion=None, cantidad_parqueaderos=None,
                    inmueble_nuevo=0, barrio = None):
    detalles = sopa.find("div", class_="details").findAll("span")

    data = sopa.find("div", class_="data")  # Inicializo un conjunto de datos

    try:
        if data.findAll("h2")[1].text != "":
            barrio = data.findAll("h2")[1].text
    except:
        print("Rechazado por barrio nulo")
        return None

    if municipio == medellin:
        zonaEncontrada = 0
        for listaActZona in [Medellín_Nororiental, Medellín_Noroccidental, Medellín_Centroriental,
                             Medellín_Centroccidental, Medellín_Suroriental, Medellín_Suroccidental,
                             Medellín_Rural]:
            if barrio in listaActZona:
                municipioCarta = listaActZona[0]
                zonaEncontrada = 1
        if not zonaEncontrada:
            print("Rechazado por barrio rezagado,", barrio)
            return None

    inith4 = data.findAll("h4")  # Inicializo un conjunto de datos
    h4 = [h.text.split(":") for h in inith4]
    if len(h4) != 3:
        print("Rechazado por area, habitaciones o banos")
        return None
    area_total = round(float(h4[0][1][:-3]), 2)
    cantidad_habitaciones = int(h4[1][1])
    cantidad_banos = int(h4[2][1])

    try:
        nombre_publicacion = data.find("h1").text
    except:
        print("Rechazado por nombre_publicacion")
        return None

    try:
        tipo_inmueble = data.find("h1").text.split(" en Venta", 1)[0]
    except:
        print("Rechazado por tipo_inmueble")
        return None

    try:
        valor_inmueble = int("".join(i for i in data.find("h3").text[1:].split(".")))
    except:
        print("Rechazado por valor_inmueble")
        return None

    try:
        descripcion = sopa.find("div", class_="txt-general").text
    except:
        descripcion = None

    try:
        vendedor = sopa.find("div", class_="agent").find("h3").text
    except:
        vendedor = None

    try:
        imagen_inmueble = "https://www.appropiate.com/" + sopa.find("a", class_="item lightbox")["href"]
    except:
        print("Rechazado por imagen")
        return None

    antiguedadNula = 0
    for i, x in enumerate(detalles):
        if i % 2 != 0:
            act = x.text.split(" ")
            if act[-1] == "Parqueadero" or act[-1] == "Parqueaderos":
                cantidad_parqueaderos = int(act[0])
            if act[0].split("$")[0] == "Administración":
                costo_administracion = int("".join(act[0].split("$")[1].split(".")))
            if act[-1] == "años":
                inmueble_nuevo = 0
                antiguedadNula = 0
            if act[-1] == "año":
                inmueble_nuevo = 1
                antiguedadNula = 0
    if antiguedadNula:
        inmueble_nuevo = 2

    # Correcciones de strings para normalizar

    if not tipo_inmueble in tiposInmuebles and not tipo_inmueble in inmueblesDesconocidos:
        inmueblesDesconocidos.append(tipo_inmueble)
    # Hotel/Apart Hotel es edificio
    # edificio es ???
    if tipo_inmueble == "Finca Recreativa" or tipo_inmueble == "Finca en Parcelacion" \
            or tipo_inmueble == "Finca Productiva":
        tipo_inmueble = "Finca"
    elif tipo_inmueble == "Lote Industrial" or tipo_inmueble == "Lote Independiente" \
            or tipo_inmueble == "Lote Comercial" or tipo_inmueble == "Lote en Parcelación":
        tipo_inmueble = "Lote"
    elif tipo_inmueble == "Apartaestudio":
        tipo_inmueble = "Apartamento"
    elif tipo_inmueble == "Casa Local":
        tipo_inmueble = "Casa"
    elif tipo_inmueble == "Local Comercial" or tipo_inmueble == "Cowork":
        tipo_inmueble = "Local"

    if municipioCarta == "Medell%C3%ADn":
        municipioCarta = "Medellín"
        print("El municipio es medellin, dado que el barrio es:", barrio)
    elif municipioCarta == "La+Estrella":
        municipioCarta = "La Estrella"

    return {
        "nombre_fuente": "Appropiate.com",
        "nombre_publicacion": nombre_publicacion,
        "url_fuente": linkCarta,
        "tipo_inmueble": tipo_inmueble,
        "valor_inmueble": valor_inmueble,
        "municipio": municipioCarta,
        "barrio": barrio,
        "cantidad_habitaciones": cantidad_habitaciones,
        "area_total": area_total,
        "area_construida": None,  # Nunca observado
        "descripcion": descripcion,
        "vendedor": vendedor,
        "cantidad_banos": cantidad_banos,
        "costo_administracion": costo_administracion,
        "cantidad_parqueaderos": cantidad_parqueaderos,
        "costo_servicios_publicos": None,  # Nunca observado
        "estrato": None,  # Nunca observado
        "inmueble_nuevo": inmueble_nuevo,
        "imagen_inmueble": imagen_inmueble
    }


headers = {"User-agent": "Mozilla/5.0"}
medellin = "Medell%C3%ADn"
municipios = [medellin, "Bello", "Itagüí", "Envigado", "Sabaneta", "Caldas", "Copacabana", "La+Estrella", "Barbosa", "Girardota"]
tiposInmuebles = ["Apartamento", "Casa", "Oficina", "Local", "Finca", "Lote", "Bodega", "Consultorio"]

inmueblesDesconocidos = []

Medellín_Nororiental = ["Medellín Nororiental", "El Chagualo", "Estación Villa", "Aranjuez", "Berlín", "La Piñuela",
                        "San Isidro", "Palermo", "Bermejal",
                        "San Pedro", "Sevilla", "Brasilia", "Manrique Central 1", "Manrique 1 Central 2",
                        "Campo Valdés 1",
                        "Campo Valdés 2", "Popular 1 y 2", "Santo Domingo Savio 1", "Santo Domingo Savio 2", "Moscú 1",
                        "Moscú 2",
                        "Granizal,", "La Isla", "El Raizal", "El Playón de los", "Comuneros 1 (La Frontera)", "Moravia",
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
Medellín_Noroccidental = ["Medellín Noroccidental", "Robledo", "Cerro El Volador", "El Cucaracho", "Palenque 1 y 2",
                          "San Germán", "La Pilanca", "El Progreso",
                          "Iguaná", "Lenin", "Aures", "Mirador del 12", "Picacho", "Picachito", "Salvador", "Allende",
                          "Jorge Eliécer",
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
                          "Monteverde", "Villaflora", "Vallejuelos", "Villa Sofía", "Romeral", "Doña María", "Robledo",
                          "Nebraska",
                          "El Cortijo", "Candelaria"]
Medellín_Centroriental = ["Medellín Centroriental", "Guayaquil", "Colón", "Sucre", "La Ladera", "El Salvador", "Loreto",
                          "Villa Hermosa", "Enciso",
                          "La Milagrosa", "Alejandro", "Echavarría", "La Mansión", "Caicedo", "La Toma", "San Diego",
                          "Las Palmas",
                          "La Independencia", "Perpetuo Socorro", "Corazón de Jesús", "Barrio Nuevo", "Llanaditas",
                          "Buenos Aires",
                          "Boston", "Prado", "Villa Nueva", "San Benito", "Candelaria", "Corazón de Jesús", "Bomboná",
                          "Los Ángeles",
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
                          "Urbanización La Palma", "Isaac Gaviria"]
Medellín_Centroccidental = ["Medellín Centroccidental", "El Salado", "Betania", "La Puerta", "La Loma", "El Corazón",
                            "Belencito", "El Coco", "El Socorro",
                            "Campo Alegre", "La América", "San Javier", "Floresta", "El Danubio", "Barrio Cristóbal",
                            "Lorena", "Laureles",
                            "Miravalle", "Florida", "Ferrini", "La Independencia 1,", "La Independencia 2",
                            "La Independencia 3",
                            "Nuevos Conquistadores", "La Colina", "Fuente Clara", "Blanquizal", "La Quiebra",
                            "Santa Rosa de Lima",
                            "La Pradera", "Los Alcázares", "Antonio Nariño", "Metropolitano", "20 de Julio",
                            "San Joaquín",
                            "Carlos E. Restrepo", "Santa Mónica", "Santa Lucía", "Calasanz", "Conquistadores",
                            "Velódromo",
                            "Unidad Deportiva", "Florida Nueva", "Simón Bolívar", "Bolivariana", "Suramericana"]
Medellín_Suroriental = ["Medellín Suroriental", "Loma de los Parra", "Loma de Los González", "El Garabato", "El Tesoro",
                        "Loma de Los Mangos", "La Chacona",
                        "El Poblado", "Aguacatala", "Castropol", "Patio Bonito", "LLeras", "Santa María de los Ángeles",
                        "Villa Carlota", "Barrio Colombia", "Manila", "Astorga", "Provenza", "Alejandría", "Los Balsos",
                        "Las Lomas",
                        "Altos del Poblado", "San Lucas", "Florida", "El Castillo", "El Diamante", "Los Naranjos",
                        "El Remanso",
                        "El Futuro", "Guadalajara", "Vegas del Poblado"]
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
                          "El Rodeo", "Loma de los Bernal"]
Medellín_Rural = ["Medellín Rural", "Altavista", "Palmitas", "Santa Elena", "San Cristóbal", "San Antonio de Prado"]

pasan = 0
rechazados = 0
cont = 0
for municipio in municipios:
    linkBase = "https://www.appropiate.com/buscador?" \
               "q_str=" + municipio + \
               "&q_label=&q_value=&concepto=2&tipo_inmueble[]=38&tipo_inmueble[]=2&tipo_inmueble[]=27&tipo_inmueble[]=33&tipo_inmueble[]=40&tipo_inmueble[]=29&tipo_inmueble[]=41&tipo_inmueble[]=30&tipo_inmueble[]=39&tipo_inmueble[]=31&tipo_inmueble[]=35&tipo_inmueble[]=32&tipo_inmueble[]=26&tipo_inmueble[]=28&tipo_inmueble[]=37&tipo_inmueble[]=34&tipo_inmueble[]=36&tipo_inmueble[]=25" \
               "&q=" + municipio + \
               "&busqueda=1" \
               "&pag="
    pagina = 0
    while 1:  # Iterar entre paginas.
        pagina += 1
        linkAct = linkBase + str(pagina)  # linkAct es el link correspondiente a la pagina j

        peticion = requests.get(linkAct, headers=headers)  # Se realiza la peticion a appropiate

        soup = BeautifulSoup(peticion.content, "html.parser")  # Se obtiene el html

        listaInmuebles = soup.find_all("a", class_="m-inm")
        if not listaInmuebles:
            # No hay más inmuebles, o sea, no hay mas paginas
            break  # Siguiente municipio

        listaCartas = [s["href"] for s in
                       listaInmuebles]  # Se obtienen los links de todos los inmuebles/cartas de la pagina

        enlace: "str"
        for enlace in listaCartas:
            peticionCarta = requests.get(enlace, headers=headers)
            soupAux = BeautifulSoup(peticionCarta.content, "html.parser")
            inmuebleAct = cartaPorcesador(soupAux, enlace, municipio)
            cont += 1
            if inmuebleAct is not None:
                pasan += 1
                print(inmuebleAct)
            else:
                rechazados += 1
print("Aceptados:", pasan,"---Rechazados:", rechazados,"---Porcentaje aceptados:", round((pasan / cont)*100,2),"---Porcentaje rechazados:", round((rechazados / cont)*100,2))
print("Inmuebles desconocidos:", inmueblesDesconocidos)
