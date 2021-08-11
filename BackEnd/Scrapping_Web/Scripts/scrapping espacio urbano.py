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
            Inmuebles_Espacio_Urbano(BS,server)
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

# En el siguiente metodo buscamos como tal los links en cada pagina que se recibe
# luego ingresamos a estos links y obtenemos la información como tal que buscamos


def Inmuebles_Espacio_Urbano(BS,server):
    inmuebles_raw = BS.find_all('table', {'class': 'Destacado'})
    # print('Inmuebles:',len(inmuebles_raw))
    register = {}
    for i in inmuebles_raw:
        # start = datetime.datetime.now()
        link_inmueble = server+str(i.a['href'])
        link_problem.clear()
        link_problem.setdefault(link_inmueble, link_inmueble)
        if (link_inmueble in visited_Espacio_Urbano or link_inmueble in problematic_links):
            continue
        inmueble = BeautifulSoup(get_data_tiempo(link_inmueble), "html5lib")
        print('Link: ', link_inmueble)
        try:
            center_info = inmueble.find_all('div', {'class': 'text-center'})[1].find_all('h3')
        except Exception as ex:
            print('Except center_info:', ex, 'Link:', link_inmueble)
            problematic_links.append(link_inmueble)
            continue
        print('Titulo:',center_info[2].text)
        print('Precio:',center_info[0].text.split('$')[1])

        try:
            description = inmueble.find('div',{'align':'justify'})
        except Exception as ex:
            print('Except description:', ex, 'Link:', link_inmueble)
            problematic_links.append(link_inmueble)
            continue
        print('Descripción:',description.text)
        extras = []
        try:
            extras_raw = inmueble.find('div',{'class':'col-sm-4'}).find_all('p')
            for i in extras_raw:
                if (len(i)!=0 and len(i)>1):
                    extras.append(i)
        except Exception as ex:
            print('Except extras:', ex, 'Link:', link_inmueble)
            problematic_links.append(link_inmueble)
            continue
        
        if (len(extras)!=0):
            for i in extras:
                print(i.text)        

if __name__ == '__main__':
    Lista_Inmuebles_Espacio_Urbano()
