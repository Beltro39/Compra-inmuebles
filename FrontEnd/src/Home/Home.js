import houses from '../assets/casa.jpg';
import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import { Pagination } from '@material-ui/lab';
import Gridcards from './Gridcards';
import Listcards from './Listcards';
import Slider from '../Slider/Slider';
import { GiChainsaw, GiMachete } from "react-icons/gi";
import { useAuth0 } from '@auth0/auth0-react';

function Home() {
  const { isAuthenticated } = useAuth0();
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

  const [buttonFilter] = useState("Aplicar filtros");
  const [buttonName, setButtonName] = useState(<span><GiChainsaw/> Cambiar a cuadricula</span>);
  const [showListView, setShowListView] = useState(true);

  function applyFilters() {

    console.log("Cualquier filtro :v")
  }

  function changeView() {
    setShowListView(!showListView)
    setButtonName(showListView ? <span><GiMachete/> Cambiar a listado</span> : <span><GiChainsaw/> Cambiar a cuadricula</span>)
    console.log("Cualquier texto :v", buttonName)
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
              <div className="form-check">
                <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                <label className="form-check-label" htmlFor="flexCheckDefault" style={styles.styleLabel}>
                  Apartamento
                </label>
              </div>

              <div className="form-check">
                <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                <label className="form-check-label" htmlFor="flexCheckDefault" style={styles.styleLabel}>
                  Apartaestudio
                </label>
              </div>

              <div className="form-check">
                <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                <label className="form-check-label" htmlFor="flexCheckDefault" style={styles.styleLabel}>
                  Casa
                </label>
              </div>

              <div className="form-check">
                <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                <label className="form-check-label" htmlFor="flexCheckDefault" style={styles.styleLabel}>
                  Local
                </label>
              </div>

              <div className="form-check mb-3">
                <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                <label className="form-check-label" htmlFor="flexCheckDefault" style={styles.styleLabel}>
                  Oficina
                </label>
              </div>
            </div>
            <br></br>

            {/* Contenedor del precio */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Precio</h4>
              <div className="form-floating mb-3">
                <input type="number" className="form-control" id="floatingInput" placeholder="Desde: "></input>
              </div>

              <div className="form-floating mb-3">
                <input type="number" className="form-control" id="floatingInput" placeholder="Hasta: "></input>
              </div>
            </div>
            <br></br>

            {/* Contenedor del tamaño en metros cuadrados */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Tamaño en M2</h4>
              <div className="form-floating mb-3">
                <input type="number" className="form-control" id="floatingInput" placeholder="Desde: "></input>
              </div>

              <div className="form-floating mb-3">
                <input
                  type="number" className="form-control" id="floatingInput" placeholder="Hasta: "></input>
              </div>
            </div>
            <br></br>

            {/* Contenedor del checkbox para la cantidad de baños */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Cantidad de baños</h4>

              <select className="form-select form-select-sm mb-3" placeholder="Seleccione cantidad de baños" aria-label=".form-select-sm example" style={{ fontSize: "15px", width: "100%", borderRadius: ".25rem", height: "calc(1.5em + .75rem + 2px)" }}>
                <option value="1" style={styles.styleLabel}>1 o más</option>
                <option value="2" style={styles.styleLabel}>2 o más</option>
                <option value="3" style={styles.styleLabel}>3 o más</option>
                <option value="4 o más" style={styles.styleLabel} >4 o más</option>
              </select>

            </div>

            <br></br>

            {/* Contenedor del checkbox para la cantidad de habitaciones */}
            <div className="container-fluid" style={styles.styleForm}>
              <h4 style={styles.styleTitle}>Cantidad de habitaciones</h4>
              <select className="form-select form-select-sm mb-3" placeholder="Seleccione cantidad de baños" aria-label=".form-select-sm example" style={{ fontSize: "15px", width: "100%", borderRadius: ".25rem", height: "calc(1.5em + .75rem + 2px)" }}>
                <option value="1" style={styles.styleLabel}>1 o más</option>
                <option value="2" style={styles.styleLabel}>2 o más</option>
                <option value="3" style={styles.styleLabel}>3 o más</option>
                <option value="4 o más" style={styles.styleLabel} >4 o más</option>
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
                showListView ? showListedElements() : showMoreElements()
              }
            </div>


          </div>

        </div>


        <br></br>
      </div>
    </div>
  );
}

//Función para mostrar los inmuebles en forma de listado
function showListedElements() {
  return (
    <div >
      <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
      <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
      <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
      <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />

      <div className="Home-Footer" >
        <div className="row justify-content-center">
          <Pagination count={10} color="primary" />
        </div>
      </div>
    </div>
  )
}

//Función para mostrar los inmuebles en forma de cuadricula
function showMoreElements() {
  return (

    <div >
      <div className="row">
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
      </div>
      <div className="Home-Footer" >
        <div className="row justify-content-center">
          <Pagination count={10} color="primary" />
        </div>
      </div>
    </div>

  );
}

export default Home;
