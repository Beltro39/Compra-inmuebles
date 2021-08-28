import './Slider.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import SliderCard from './SliderCard';
import React, { useEffect, useState } from 'react';

function Slider() {

    const [infoInmueble, setInfoInmueble] = useState([]);
    const [isLoad, setIsLoad] = useState(false);

    async function apiRestList() {
        return fetch('https://201.184.129.122/FrancaPaisa-Servicios/v0/francapaisa-inmuebles/scrapping/?pageSize=300&pageNumber=1')
            .then(response => response.json())
            .then(data => {
                let dataMaped = data.map((element) => {
                    if (element.nombre_fuente === "Properati") {
                        element.url_fuente = "https://www.properati.com.co" + element.url_fuente;
                    } else if (element.nombre_fuente === "https://habitamos.com.co/") {
                        element.nombre_fuente = "habitamos";
                    } else if (element.nombre_fuente === "espaciourbano.com") {
                        element.nombre_fuente = "espaciourbano";
                    }
                    element.nombre_fuente = element.nombre_fuente.charAt(0).toUpperCase() + element.nombre_fuente.slice(1);
                    return element;
                });
                setInfoInmueble(dataMaped);
                setIsLoad(true);
            })
    }

    useEffect(() => {
        apiRestList();
    }, [])

    if (isLoad) {

        return (

            <div id="mycarousel" className="carousel slide" data-ride="carousel">
                <div className="carousel-inner" role="listbox">
                    <div className="carousel-item active">
                        <SliderCard key={infoInmueble[9].idScrapping} img={infoInmueble[9].imagen_inmueble} lugar={infoInmueble[9].barrio_data.nombre}
                            tipo={infoInmueble[9].tipo_inmueble_data.nombre} precio={infoInmueble[9].valor_inmueble} fuente={infoInmueble[9].nombre_fuente}
                            url={infoInmueble[9].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[10].idScrapping} img={infoInmueble[10].imagen_inmueble} lugar={infoInmueble[10].barrio_data.nombre}
                            tipo={infoInmueble[10].tipo_inmueble_data.nombre} precio={infoInmueble[10].valor_inmueble} fuente={infoInmueble[10].nombre_fuente}
                            url={infoInmueble[10].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[11].idScrapping} img={infoInmueble[11].imagen_inmueble} lugar={infoInmueble[11].barrio_data.nombre}
                            tipo={infoInmueble[11].tipo_inmueble_data.nombre} precio={infoInmueble[11].valor_inmueble} fuente={infoInmueble[11].nombre_fuente}
                            url={infoInmueble[11].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[12].idScrapping} img={infoInmueble[12].imagen_inmueble} lugar={infoInmueble[12].barrio_data.nombre}
                            tipo={infoInmueble[12].tipo_inmueble_data.nombre} precio={infoInmueble[12].valor_inmueble} fuente={infoInmueble[12].nombre_fuente}
                            url={infoInmueble[12].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[13].idScrapping} img={infoInmueble[13].imagen_inmueble} lugar={infoInmueble[13].barrio_data.nombre}
                            tipo={infoInmueble[13].tipo_inmueble_data.nombre} precio={infoInmueble[13].valor_inmueble} fuente={infoInmueble[13].nombre_fuente}
                            url={infoInmueble[13].url_fuente} />
                    </div>
                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[14].idScrapping} img={infoInmueble[14].imagen_inmueble} lugar={infoInmueble[14].barrio_data.nombre}
                            tipo={infoInmueble[14].tipo_inmueble_data.nombre} precio={infoInmueble[14].valor_inmueble} fuente={infoInmueble[14].nombre_fuente}
                            url={infoInmueble[14].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[15].idScrapping} img={infoInmueble[15].imagen_inmueble} lugar={infoInmueble[15].barrio_data.nombre}
                            tipo={infoInmueble[15].tipo_inmueble_data.nombre} precio={infoInmueble[15].valor_inmueble} fuente={infoInmueble[15].nombre_fuente}
                            url={infoInmueble[15].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[16].idScrapping} img={infoInmueble[16].imagen_inmueble} lugar={infoInmueble[16].barrio_data.nombre}
                            tipo={infoInmueble[16].tipo_inmueble_data.nombre} precio={infoInmueble[16].valor_inmueble} fuente={infoInmueble[16].nombre_fuente}
                            url={infoInmueble[16].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[17].idScrapping} img={infoInmueble[17].imagen_inmueble} lugar={infoInmueble[17].barrio_data.nombre}
                            tipo={infoInmueble[17].tipo_inmueble_data.nombre} precio={infoInmueble[17].valor_inmueble} fuente={infoInmueble[17].nombre_fuente}
                            url={infoInmueble[17].url_fuente} />
                    </div>

                    <div className="carousel-item ">
                        <SliderCard key={infoInmueble[19].idScrapping} img={infoInmueble[19].imagen_inmueble} lugar={infoInmueble[19].barrio_data.nombre}
                            tipo={infoInmueble[19].tipo_inmueble_data.nombre} precio={infoInmueble[19].valor_inmueble} fuente={infoInmueble[19].nombre_fuente}
                            url={infoInmueble[19].url_fuente} />
                    </div>
                </div>
                <ol className="carousel-indicators">
                    <li data-target="#mycarousel" data-slide-to="0" className="active"></li>
                    <li data-target="#mycarousel" data-slide-to="1"></li>
                    <li data-target="#mycarousel" data-slide-to="2"></li>
                    <li data-target="#mycarousel" data-slide-to="3"></li>
                    <li data-target="#mycarousel" data-slide-to="4"></li>
                    <li data-target="#mycarousel" data-slide-to="5"></li>
                    <li data-target="#mycarousel" data-slide-to="6"></li>
                    <li data-target="#mycarousel" data-slide-to="7"></li>
                    <li data-target="#mycarousel" data-slide-to="8"></li>
                    <li data-target="#mycarousel" data-slide-to="9"></li>
                </ol>
                <a className="carousel-control-prev" href="#mycarousel" role="button" data-slide="prev">
                    <span className="carousel-control-prev-icon"></span>
                </a>
                <a className="carousel-control-next" href="#mycarousel" role="button" data-slide="next">
                    <span className="carousel-control-next-icon"></span>
                </a>


            </div>

        );
    } else {
        return (
            <div></div>
        )
    }
}

export default Slider;


