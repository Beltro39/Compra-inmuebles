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
            color: "white"
        },
    }

    return (
        <div className="Login" >
            <header className="Login-header">
                <br></br>
                <div className="row justify-content-center">
                    <div className="col-lg-6 col-10 col-sm-8">
                        <div className="container" style={styles.styleForm}>
                            <div className="row justify-content-center" style={styles.styleFormHeader}>
                                Iniciar Sesión
                            </div>
                            
                            <form class="justify-content-center">

                                <div className="form-group mt-4">
                                    <label>Correo</label>
                                    <input type="email" className="form-control" />
                                </div>

                                <div className="form-group mt-5">
                                    <label>Contraseña</label>
                                    <input type="password" className="form-control" />
                                </div>

                                <div className="row justify-content-center mt-5 ">
                                <button type="submit" className="btn" style={styles.styleButton}>Iniciar Sesión</button>
                                </div>

                                <p className="forgot-password mt-4">
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