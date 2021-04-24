import './Home.css';
import 'bootstrap/dist/css/bootstrap.min.css';

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
  };
  return (
    <div className="Home">
      <header className="Home-header">
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

                <div className="form-check">
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

                <div className="form-check">
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

                <div className="form-check">
                  <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault"></input>
                  <label className="form-check-label" for="flexCheckDefault" style={styles.styleLabel}>
                    Más de cuatro
                  </label>
                </div>
              </div>
              <br></br>
            </div>

            <div className="col-sm-auto" style={styles.styleForm}>
              <p>Imagenes de inmuebles</p>
            </div>

          </div>

        </div>
        <br></br>
      </header>
    </div>
  );
}

export default Home;
