import './Register.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function Register() {

    const styles = {
        styleForm: {
            border: '2px solid grey',
        },
        styleLabel: {
            fontSize: '15px',
            marginTop: 10,
            marginBottom: 4
        },
        styleFormHeader: {
            backgroundColor: "blue"
        },
        styleButton: {
            marginBottom: 5,
            backgroundColor: "blue"
        },
    }

    return (
        <div className="Register">
            <header className="Register-header">
                <br></br>
                <div className="row justify-content-center">
                    <div className="col-md-6">
                        <div className="container" style={styles.styleForm}>
                            <div className="row justify-content-center" style={styles.styleFormHeader}>
                                Registrarse
                                </div>
                            <br></br>
                            <form>

                                <div className="form-group">
                                    <label>Nombre</label>
                                    <input type="text" className="form-control" />
                                </div>

                                <div className="form-group">
                                    <label>Apellido</label>
                                    <input type="text" className="form-control" />
                                </div>

                                <div className="form-group">
                                    <label>Correo</label>
                                    <input type="email" className="form-control" />
                                </div>

                                <div className="form-group">
                                    <label>Contraseña</label>
                                    <input type="password" className="form-control" />
                                </div>

                                <br></br>
                                <button type="submit" className="btn btn-primary btn-block" style={styles.styleButton}>Registrarse</button>
                                <br></br>
                                <p className="forgot-password">
                                    ¿Ya se encuentra registrado? <a href="/login">Iniciar Sesión</a>
                                </p>
                            </form>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    );
}

export default Register;
