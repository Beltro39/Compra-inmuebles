import './AboutUs.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Area from '../assets/Area.png';
import paginasUsadas from '../assets/paginas.png';
import equipo from '../assets/equipo.png';

function AboutUs() {
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

    return (
        <div className="container">
            <header className="AboutUs-header">
                <div className="row justify-content-center">
                <br></br>
                    <div className="row">
                        <div className="col-sm-5" style={styles.styleForm}>
                            <p>¿Quienes Somos?</p>
                            <br></br>
                            <p className="AboutUs" >FRANCA PAISA es un Portal Web
                            en Colombia dedicado a la búsqueda,
                            análisis, clasificación y sugerencia
                            de inmuebles según las especificaciones
                            requeridas en la búsqueda hecha por el
                            interesado en Bienes Raíces.
                            </p>
                            <br></br>
                            <p className="AboutUs" >
                                FRANCAPAISA.co te ofrece en el Área Metropolitana
                                del Valle de Aburrá, inmuebles en venta.
                            </p>
                            <img src={Area} className="AreaMetropolitana" alt="logo" />
                            <br></br>
                            <br></br>
                            <p className="AboutUs" >
                                Recopilamos inmuebles de ocho páginas para ahorrarte tiempo en la búsqueda.
                            </p>

                        </div>
                        <div className="col-sm-7" style={styles.styleForm}>
                            <img src={paginasUsadas} className="paginasUsadas" alt="logo" />
                            <img src={equipo} className="equipo" alt="logo" />


                        </div>
                    </div>
                </div>

            </header>
        </div>
    );
}
export default AboutUs;
