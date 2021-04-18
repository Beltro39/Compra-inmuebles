import './AboutUs.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { GoLocation } from 'react-icons/go';
import { BiPhoneCall } from 'react-icons/bi';
import { AiFillRead, AiOutlineQuestionCircle } from 'react-icons/ai';
import { Button } from 'react-bootstrap';


function AboutUs() {
  const styles = {
    styleIframe: {
        border: '2px solid blue',
    },
    styleForm: {
        border: '2px solid grey',
        marginRigth: 5
    },
    styleLabel: {
        fontSize: '15px',
        marginTop: 10,
        marginBottom: 4
    },
    styleButton: {
        marginBottom: 5
    },
    styleIcons: {
        marginBottom: 1,
        color: "blue"
    },
    styleContactInfo: {
        paddingBottom: 5
    },
    styleFormHeader: {
        backgroundColor: "blue"
    }
};

return (
  <div className="container" style={styles.styleForm}>
      <header className="AboutUs-header">
          
      <div className="row">
        <div className="col-5" style={styles.styleForm}>
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
             <img src="banner.png" class="img-fluid"></img>
             <br></br>
             <p className="AboutUs" >
             Recopilamos inmuebles de ocho páginas para ahorrarte tiempo en la búsqueda.
             </p>
        </div>
        <div className="col-7" style={styles.styleForm}>
        <img src="paginas.png" class="img-fluid"></img>
        <img src="equipo.png" class="img-fluid"></img>

        </div>
      </div>

      </header>
  </div>
);
}
export default AboutUs;
