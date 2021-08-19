import 'bootstrap/dist/css/bootstrap.min.css';
import './Contact.css';

// CommonJS





function Contact() {
    const Swal = require('sweetalert2');


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
            marginBottom: 5,
            backgroundColor: "blue",
            justifyContent: 'center',
        }
    };

    return (
        <div className="Contact">
            <header className="Contact-header">
                <br></br>
                <div className="row justify-content-center">

                    <div className="col-md-auto" >
                        <iframe title="google-map-code" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d63456.599682455846!2d-75.63525554822925!3d6.258793413644702!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e4428e678fd90af%3A0x483eb5aade56b0b!2sUniversidad%20Nacional%20de%20Colombia%20Sede%20Medell%C3%ADn!5e0!3m2!1ses!2sco!4v1618674031699!5m2!1ses!2sco" width="800" height="650" style={styles.styleIframe}></iframe>
                    </div>

                    <div className="col-md-4">
                        <form className="g-3 needs-validation"  id="myform">
                            <div className="container" style={styles.styleForm}>
                                <div className="row justify-content-center" style={styles.styleFormHeader}>
                                    Dejanos un mensaje, nuestro equipo se pondra en contacto contigo
                                </div>
                                <br></br>
                                <div>
                                    <div className="form-group">
                                        <label>Nombre</label>
                                        <input type="text" id="name" pattern="[a-zA-Z]*" title="Este campo solo permite letras" className="form-control" required />
                                    </div>

                                    <div className="form-group">
                                        <label>Correo electrónico</label>
                                        <input type="email" pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" title="Por favor introduza un correo válido" className="form-control" required />
                                    </div>

                                    <div className="form-group">
                                        <label>Telefono</label>
                                        <input type="text" pattern="[0-9]*" title="Este campo solo permite numeros" className="form-control" required />
                                    </div>

                                    <div className="form-group">
                                        <label>Descripción</label>
                                        <textarea type="text" className="form-control" required />
                                    </div>

                                    <br></br>
                                    <button onClick={(event) => { 
                                        event.preventDefault();
                                        if (document.getElementById("myform").checkValidity()) {
                                            Swal.fire({
                                                background: '#282c34',
                                                text: 'Mensaje enviado exitosamente'
                                            })
                                        }
                                        document.getElementById("myform").reset()
                                    }} type="submit" className="btn btn-primary btn-block" style={styles.styleButton}>Enviar</button>
                                    <br></br>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </header>
        </div >
    );
}

export default Contact;
