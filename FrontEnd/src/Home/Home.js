import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";
import Loader from "react-loader-spinner";
import React, { useEffect, useState } from 'react';
import { Pagination } from '@material-ui/lab';
import Gridcards from './Gridcards';
import Listcards from './Listcards';
import Slider from '../Slider/Slider';
import { GiChainsaw, GiMachete } from "react-icons/gi";
import { useAuth0 } from '@auth0/auth0-react';



function Home() {
  const { isAuthenticated } = useAuth0();
  const [buttonFilter] = useState("Aplicar filtros");
  const [buttonName, setButtonName] = useState(<span><GiChainsaw /> Cambiar a cuadricula</span>);
  const [showListView, setShowListView] = useState(true);
  const [tipo_inmueble, setType] = useState(1);
  const [valor_inmueble_min, setMinValue] = useState(0);
  const [valor_inmueble_max, setMaxValue] = useState(0);
  const [area_total_min, setMinSize] = useState(0);
  const [area_total_max, setMaxSize] = useState(0);
  const [cantidad_banos, setBanos] = useState(1);
  const [cantidad_habitaciones, setRooms] = useState(1);
  function handleType(event) {
    setType(event.target.value);
  }
  function handleMinValue(event) {
    setMinValue(event.target.value);
  }
  function handleMaxValue(event) {
    setMaxValue(event.target.value);
  }
  function handleMinSize(event) {
    setMinSize(event.target.value);
  }
  function handleMaxSize(event) {
    setMaxSize(event.target.value);
  }
  function handleBanos(event) {
    setBanos(event.target.value);
  }
  function handleRooms(event) {
    setRooms(event.target.value);
  }


  const [infoInmueble, setInfoInmueble] = useState([])

  const [isLoad, setIsLoad] = useState(false);

  const [tiposInmuble, setTiposInmueble] = useState([])
  async function apiRestTypes() {
    return fetch('https://201.184.129.122/FrancaPaisa-Servicios/v0/francapaisa-inmuebles/tipo-inmueble/')
      .then(response => response.json())
      .then(data => {
        setTiposInmueble(data)
      })
  }
  async function apiRestList() {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tipo_inmueble: null,
        valor_inmueble_min: null,
        valor_inmueble_max: null,
        area_total_min: null,
        area_total_max: null,
        cantidad_banos: null,
        cantidad_habitaciones: null
      })
    };

    return fetch('https://201.184.129.122/FrancaPaisa-Servicios/v0/francapaisa-inmuebles/scrapping/', requestOptions)
      .then(response => response.json())
      .then(data => {
        setInfoInmueble(data)
        setIsLoad(true)
      })
  }

  useEffect(() => {
    apiRestList();
    apiRestTypes();
  }, [])


  const styles = {

    styleFormFilter: {
      border: "1px solid grey",
      textAlign: "left",
      marginRight: "50px"
    },

    styleForm: {
      border: "1px solid grey",
      textAlign: "left",
    },

    styleLabel: {
      fontSize: "15px",
      textAlign: "left",
    },

    styleFormHeader: {
      backgroundColor: "blue",
    },

    styleTitle: {
      textAlign: "center",
      fontWeight: "bold",
    },
  };

  function applyFilters() {

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        tipo_inmueble,
        valor_inmueble_min,
        valor_inmueble_max,
        area_total_min,
        area_total_max,
        cantidad_banos,
        cantidad_habitaciones
      })
    };

    return fetch('https://201.184.129.122/FrancaPaisa-Servicios/v0/francapaisa-inmuebles/scrapping/', requestOptions)
      .then(response => response.json())
      .then(data => {
        setInfoInmueble(data)
        setIsLoad(true)
      })
  }

  function changeView() {


    setShowListView(!showListView)
    setButtonName(showListView ? <span><GiMachete /> Cambiar a listado</span> : <span><GiChainsaw /> Cambiar a cuadricula</span>)

  }
  return (

    <div className="container Home">

      <div className="row justify-content-left">

        {
          isAuthenticated ? (<Slider></Slider>) : ('')
        }


        <div className="row">

          {/* Contenedor de los filtros */}
          <div className="col-md-auto" style={styles.styleFormFilter}>
            <p style={styles.styleTitle}>Filtros</p>

            {/* Contenedor de los checkbox para el tipo de inmueble */}
            <div className="container" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Tipo de inmueble</h4>
              <div>
                <select value={tipo_inmueble} onChange={handleType} className="form-select form-select-sm mb-3" placeholder="Seleccione tipo de inmueble" aria-label=".form-select-sm example" style={{ fontSize: "15px", width: "100%", borderRadius: ".25rem", height: "calc(1.5em + .75rem + 2px)" }}>
                  {
                    tiposInmuble.map(type => <option key={type.idTipoInmueble} value={type.idTipoInmueble} style={styles.styleLabel}>{type.nombre}</option>)
                  }
                </select>
              </div>
            </div>
            <br></br>

            {/* Contenedor del precio */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Precio</h4>
              <div className="form-floating mb-3">
                <input type="number" value={valor_inmueble_min} onChange={handleMinValue} className="form-control" id="floatingInput" placeholder="Desde: "></input>
              </div>

              <div className="form-floating mb-3">
                <input type="number" value={valor_inmueble_max} onChange={handleMaxValue} className="form-control" id="floatingInput" placeholder="Hasta: "></input>
              </div>
            </div>
            <br></br>

            {/* Contenedor del tamaño en metros cuadrados */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Tamaño en M2</h4>
              <div className="form-floating mb-3">
                <input type="number" value={area_total_min} onChange={handleMinSize} className="form-control" id="floatingInput" placeholder="Desde: "></input>
              </div>

              <div className="form-floating mb-3">
                <input
                  type="number" value={area_total_max} onChange={handleMaxSize} className="form-control" id="floatingInput" placeholder="Hasta: "></input>
              </div>
            </div>
            <br></br>

            {/* Contenedor del checkbox para la cantidad de baños */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Cantidad de baños</h4>

              <select value={cantidad_banos} onChange={handleBanos} className="form-select form-select-sm mb-3" placeholder="Seleccione cantidad de baños" aria-label=".form-select-sm example" style={{ fontSize: "15px", width: "100%", borderRadius: ".25rem", height: "calc(1.5em + .75rem + 2px)" }}>
                <option value="1" style={styles.styleLabel}>1 o más</option>
                <option value="2" style={styles.styleLabel}>2 o más</option>
                <option value="3" style={styles.styleLabel}>3 o más</option>
                <option value="4" style={styles.styleLabel}>4 o más</option>
              </select>

            </div>

            <br></br>

            {/* Contenedor del checkbox para la cantidad de habitaciones */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Cantidad de habitaciones</h4>
              <select value={cantidad_habitaciones} onChange={handleRooms} className="form-select form-select-sm mb-3" placeholder="Seleccione cantidad de habitaciones" aria-label=".form-select-sm example" style={{ fontSize: "15px", width: "100%", borderRadius: ".25rem", height: "calc(1.5em + .75rem + 2px)" }}>
                <option value="1" style={styles.styleLabel}>1 o más</option>
                <option value="2" style={styles.styleLabel}>2 o más</option>
                <option value="3" style={styles.styleLabel}>3 o más</option>
                <option value="4" style={styles.styleLabel}>4 o más</option>
              </select>

            </div>

            <br></br>

            <button type="submit" className="btn btn-primary btn-block mb-3 d-none d-lg-block" onClick={() => applyFilters()}>
              {buttonFilter}
            </button>

          </div>
          <br></br>
        </div>

        <div className="col-sm" style={styles.styleForm}>



          <div className="container mt-3 ">
            <button type="submit" className="btn btn-primary btn-block mb-3 d-none d-lg-block" onClick={() => changeView()}>
              {buttonName}
            </button>

            <div>
              {
                showListView ? showListedElements(infoInmueble, isLoad) : showMoreElements(infoInmueble, isLoad)
              }
            </div>


          </div>

        </div>


        <br></br>
      </div>
    </div>
  );
}

function Infocards(parametro, infoInmueble, isLoaded) {

  const [currentPage, setPage] = useState(1);
  const [currentPage2, setPage2] = useState(1);
  const [offSet, setOffset] = useState(0);
  const [offSet2, setOffset2] = useState(0);

  const handlePagination = (event, value) => {
    setPage(value);
    setOffset(4 * (value - 1));
  }
  const handlePagination2 = (event, value) => {
    setPage2(value);
    setOffset2(6 * (value - 1));
  }

  if (isLoaded) {
    if (parametro) {
      return (

        <div>
          <Listcards img={infoInmueble[offSet].imagen_inmueble} lugar={infoInmueble[offSet].barrio_data.nombre} tipo={infoInmueble[offSet].tipo_inmueble_data.nombre} precio={infoInmueble[offSet].valor_inmueble} fuente={infoInmueble[offSet].nombre_fuente} />
          <Listcards img={infoInmueble[1 + offSet].imagen_inmueble} lugar={infoInmueble[offSet + 1].barrio_data.nombre} tipo={infoInmueble[offSet + 1].tipo_inmueble_data.nombre} precio={infoInmueble[offSet + 1].valor_inmueble} fuente={infoInmueble[offSet + 1].nombre_fuente} />
          <Listcards img={infoInmueble[2 + offSet].imagen_inmueble} lugar={infoInmueble[offSet + 2].barrio_data.nombre} tipo={infoInmueble[offSet + 2].tipo_inmueble_data.nombre} precio={infoInmueble[offSet + 2].valor_inmueble} fuente={infoInmueble[offSet + 2].nombre_fuente} />
          <Listcards img={infoInmueble[3 + offSet].imagen_inmueble} lugar={infoInmueble[offSet + 3].barrio_data.nombre} tipo={infoInmueble[offSet + 3].tipo_inmueble_data.nombre} precio={infoInmueble[offSet + 3].valor_inmueble} fuente={infoInmueble[offSet + 3].nombre_fuente} />

          <div className="Home-Footer" >
            <div className="row justify-content-center">
              <Pagination count={10} color="primary" page={currentPage} onChange={handlePagination} />
            </div>
          </div>
        </div>
      )
    }
    else {
      return (
        <div>
          <div className="row">
            <Gridcards img={infoInmueble[offSet2].imagen_inmueble} lugar={infoInmueble[offSet2].barrio_data.nombre} tipo={infoInmueble[offSet2].tipo_inmueble_data.nombre} precio={infoInmueble[offSet2].valor_inmueble} fuente={infoInmueble[offSet2].nombre_fuente} />
            <Gridcards img={infoInmueble[1 + offSet2].imagen_inmueble} lugar={infoInmueble[offSet2 + 1].barrio_data.nombre} tipo={infoInmueble[offSet2 + 1].tipo_inmueble_data.nombre} precio={infoInmueble[offSet2 + 1].valor_inmueble} fuente={infoInmueble[offSet2 + 1].nombre_fuente} />
            <Gridcards img={infoInmueble[2 + offSet2].imagen_inmueble} lugar={infoInmueble[offSet2 + 2].barrio_data.nombre} tipo={infoInmueble[offSet2 + 2].tipo_inmueble_data.nombre} precio={infoInmueble[offSet2 + 2].valor_inmueble} fuente={infoInmueble[offSet2 + 2].nombre_fuente} />
            <Gridcards img={infoInmueble[3 + offSet2].imagen_inmueble} lugar={infoInmueble[offSet2 + 3].barrio_data.nombre} tipo={infoInmueble[offSet2 + 3].tipo_inmueble_data.nombre} precio={infoInmueble[offSet2 + 3].valor_inmueble} fuente={infoInmueble[offSet2 + 3].nombre_fuente} />
            <Gridcards img={infoInmueble[4 + offSet2].imagen_inmueble} lugar={infoInmueble[offSet2 + 4].barrio_data.nombre} tipo={infoInmueble[offSet2 + 4].tipo_inmueble_data.nombre} precio={infoInmueble[offSet2 + 4].valor_inmueble} fuente={infoInmueble[offSet2 + 4].nombre_fuente} />
            <Gridcards img={infoInmueble[5 + offSet2].imagen_inmueble} lugar={infoInmueble[offSet2 + 5].barrio_data.nombre} tipo={infoInmueble[offSet2 + 5].tipo_inmueble_data.nombre} precio={infoInmueble[offSet2 + 5].valor_inmueble} fuente={infoInmueble[offSet2 + 5].nombre_fuente} />
          </div>
          <div className="Home-Footer" >
            <div className="row justify-content-center">
              <Pagination count={10} color="primary" page={currentPage2} onChange={handlePagination2} />
            </div>
          </div>
        </div>
      )
    }


  } else {
    return (<div >
      <div className="centrarSpinner">

        <Loader
          type="Watch"
          color="#00BFFF"
          height={200}
          width={200}
        />

      </div>
    </div>)
  }
}







//Función para mostrar los inmuebles en forma de listado
function showListedElements(infoInmueble, isLoad) {



  return (


    <div >

      {Infocards(true, infoInmueble, isLoad)}


    </div>
  )
}

//Función para mostrar los inmuebles en forma de cuadricula
function showMoreElements(infoInmueble, isLoad) {
  return (

    <div >
      {Infocards(false, infoInmueble, isLoad)}


    </div>

  );
}

export default Home;