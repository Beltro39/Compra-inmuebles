import houses from '../assets/casa.jpg';
import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React, { useState } from 'react';
import Pagination from '@material-ui/lab/Pagination';

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
      margin: "5px",
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

    stylePagination: {
      backgroundColor: "#454a55",
      color: "white",
    }
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
    <div className="Home">
      <header className="Home-header container-fluid">

        <div className="row justify-content-left">
          <br></br>
          <div className="row">

            {/* Contenedor de los filtros */}
            <div className="col-sm-auto" style={styles.styleForm}>
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


              <div class="container mt-3">
                <button type="submit" className="btn btn-primary btn-block mb-3" onClick={() => changeView()}>
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

        </div>
        <br></br>
      </header>

      <footer className= "Home-Footer" >
        <div className="row justify-content-center" style={styles.stylePagination}>
          <Pagination count={10} color="primary" />
        </div>
      </footer>

    </div>


  );
}

function showListedElements() {
  return (
    <h1>Hola</h1>
  )
}  

function showMoreElements() {
  return (
    <div>
      <div className="row form-group">
        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>








      </div>
      <div className="row form-group">


        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

      </div>



      <div className="row form-group">
        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>

        <div className="col-sm" >
          <div class="card" >
            <img class="card-img-top" src={houses} alt="Card image cap" />
            <div class="card-body bg-dark">
              <p class="card-text text-align-left"><strong>Lugar:</strong> Loma de los Bernal</p>
              <p class="card-text text-align-left"><strong>Tipo:</strong> Casa</p>
              <p class="card-text text-align-left"><strong>Precio:</strong> 350'000.000</p>
              <p class="card-text text-align-left"><strong>Fuente:</strong> Fincaraiz.com</p>
              <a href="#" class="btn btn-primary">Más informaciom</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;