import 'bootstrap/dist/css/bootstrap.min.css';
import './Login.css';

function Login() {

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
            backgroundColor: "blue",
            justifyContent: 'center',
        }
    }

    return (
        <div className="Login" >
            <header className="Login-header">
                <br></br>
                <div className="row justify-content-center">
                    <div className="col-md-6">
                        <div className="container" style={styles.styleForm}>
                            <div className="row justify-content-center" style={styles.styleFormHeader}>
                                Iniciar Sesión
                            </div>
                            <br></br>
                            <form>

                                <div className="form-group">
                                    <label>Correo</label>
                                    <input type="email" className="form-control" />
                                </div>

                                <div className="form-group">
                                    <label>Contraseña</label>
                                    <input type="password" className="form-control" />
                                </div>

                                <br></br>
                                <button type="submit" className="btn btn-primary btn-block" style={styles.styleButton}>Iniciar Sesión</button>
                                <br></br>
                                <p className="forgot-password">
                                    ¿Aun no se encuentra registrado? <a href="/FrancaPaisa/register/">Registrese aquí</a>
                                </p>
                            </form>
                        </div>
                    </div>
                </div>
            </header>
        </div>
    );
}

export default Login;