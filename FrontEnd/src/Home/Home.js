import houses from '../assets/casa.jpg';
import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import { Pagination } from '@material-ui/lab';
import Gridcards from './Gridcards';
import Listcards from './Listcards';



const styles = {
  styleForm: {
    border: '2px solid grey',
  },
  styleLabel: {
    fontSize: '15px',
  },
  styleFormHeader: {
    backgroundColor: "blue"
  }
};

function Home() {
  const styles = {
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

  const [buttonName, setButtonName] = useState("Cuadricula");
  const [showListView, setShowListView] = useState(true);

  function changeView() {
    setShowListView(!showListView)
    setButtonName(showListView ? "Listado" : "Cuadricula")
    console.log("Cualquier texto :v", buttonName)
  }

  let showString;

  return (

      <div className="container Home">

        <div className="row justify-content-left">
          <br></br>
          <div className="row">

            {/* Contenedor de los filtros */}
            <div className="col-md-auto" style={styles.styleForm}>
              <p style={styles.styleTitle}>Filtros</p>

              {/* Contenedor de los checkbox para el tipo de inmueble */}
              <div className="container-fluid" style={styles.styleForm}>
                <h4 style={styles.styleTitle}>Tipo de inmueble</h4>
                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Apartamento
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Apartaestudio
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Casa
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Local
                  </label>
                </div>

                <div className="form-check mb-3">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Oficina
                  </label>
                </div>
              </div>
              <br></br>

              {/* Contenedor del precio */}
              <div className="container-fluid" style={styles.styleForm}>
                <h4 style={styles.styleTitle}>Precio</h4>
                <div className="form-floating mb-3">
                  <input type="price" class="form-control" id="floatingInput" placeholder=""></input>
                  <label for="floatingInput" style={styles.styleLabel}>
                    Desde
                  </label>
                </div>

                <div className="form-floating mb-3">
                  <input type="price" class="form-control" id="floatingInput" placeholder=""></input>
                  <label for="floatingInput" style={styles.styleLabel}>
                    Hasta
                  </label>
                </div>
              </div>
              <br></br>

              {/* Contenedor del tamaño en metros cuadrados */}
              <div className="container-fluid" style={styles.styleForm}>
                <h4 style={styles.styleTitle}>Tamaño en M2</h4>
                <div className="form-floating mb-3">
                  <input type="price" class="form-control" id="floatingInput" placeholder=""></input>
                  <label for="floatingInput" style={styles.styleLabel}>
                    Desde
                  </label>
                </div>

                <div className="form-floating mb-3">
                  <input
                    type="price" class="form-control" id="floatingInput" placeholder=""></input>
                  <label for="floatingInput" style={styles.styleLabel}>
                    Hasta
                  </label>
                </div>
              </div>
              <br></br>

              {/* Contenedor del checkbox para la cantidad de baños */}
              <div className="container-fluid" style={styles.styleForm}>
                <h4 style={styles.styleTitle}>Cantidad de baños</h4>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Uno
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" ></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Dos
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Tres
                  </label>
                </div>

                <div className="form-check mb-3">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" ></input>
                  <label className="form-check-label" for="flexCheckDefault"
                    style={styles.styleLabel}
                  >
                    Más de cuatro
                  </label>
                </div>
              </div>
              <br></br>

              {/* Contenedor del checkbox para la cantidad de habitaciones */}
              <div className="container-fluid" style={styles.styleForm}>
                <h4 style={styles.styleTitle}>Cantidad de habitaciones</h4>
                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" ></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Uno
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" ></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Dos
                  </label>
                </div>

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" ></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Tres
                  </label>
                </div>

                <div className="form-check mb-3">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Más de cuatro
                  </label>
                </div>
              </div>
              <br></br>
            </div>

            <div className="col-sm" style={styles.styleForm}>


           
              <div class="container mt-3 ">
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

          </div>

        
        <br></br>

        
     
      
      {/* Contenedor del footer y de la paginación de las paginas */}

      
      
      

      </div>
      <footer className= "Home-Footer" >
        <div className="row justify-content-center">
         <Pagination count={10} color="primary" /> 
        </div>
      </footer>
      </div>

         



  );
}

//Función para mostrar los inmuebles en forma de listado
function showListedElements() {
  return (
    <div >
        <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>
        <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>
        <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>
        <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>
        <Listcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>
    </div>

  )
}  

//Función para mostrar los inmuebles en forma de cuadricula
function showMoreElements() {
  return (
   
    <div >
      <div class="row form-group">
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>    
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>    
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>    
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>    
        <Gridcards img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com"/>    
      </div>
    </div>

  );
}

export default Home;
