import 'bootstrap/dist/css/bootstrap.min.css';
import { Button } from 'react-bootstrap';

function Contact() {

    const styles = {
        styleIframe: {
            border: '2px solid grey',
        },
        styleForm: {
            border: '2px solid grey',
        },
        styleLabel: {
            fontSize: '15px',
        },
        styleFormHeader: {
            backgroundColor: "blue"
        },
        styleButton: {
            backgroundColor: "blue"
        }
    };

    return (
        <div className="Contact">
            <header className="Contact-header">
                <br></br>
                <div className="row justify-content-center">
                    <div className="col-md-auto" >
                        <iframe title="google-map-code" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d63456.599682455846!2d-75.63525554822925!3d6.258793413644702!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e4428e678fd90af%3A0x483eb5aade56b0b!2sUniversidad%20Nacional%20de%20Colombia%20Sede%20Medell%C3%ADn!5e0!3m2!1ses!2sco!4v1618674031699!5m2!1ses!2sco" width="600" height="450" style={styles.styleIframe}></iframe>
                    </div>
                    <div className="col-md-auto">
                        <div className="container" style={styles.styleForm}>
                            <div className="row" style={styles.styleFormHeader}>
                                Dejanos un mensaje, nuestro equipo se pondra en contacto contigo
                            </div>
                            <div className="row justify-content-center">
                                <form>
                                    <label style={styles.styleLabel}>Nombre: </label>
                                    <br></br>
                                    <input type="text" name="name" />
                                    <br></br>
                                    <label style={styles.styleLabel}>Correo: </label>
                                    <br></br>
                                    <input type="text" name="email" />
                                    <br></br>
                                    <label style={styles.styleLabel}>Telefono:</label>
                                    <br></br>
                                    <input type="text" name="phone" />
                                    <br></br>
                                    <label style={styles.styleLabel}>Descripción: </label>
                                    <br></br>
                                    <textarea type="text" name="phone" />
                                    <br></br>
                                    <Button style={styles.styleButton}>Enviar</Button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    );
}

export default Contact;
