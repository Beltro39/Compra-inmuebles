import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import { createBrowserHistory } from 'history';
import { Nav } from 'react-bootstrap';
import { AiOutlineHome, AiOutlineQuestionCircle, AiOutlineUser, AiOutlineLogout } from 'react-icons/ai';
import { BiPhoneCall } from 'react-icons/bi';
import { BsPeople } from 'react-icons/bs';
import { GoLocation } from 'react-icons/go';
import { Router, Route, Switch } from "react-router-dom";
import AboutUs from './AboutUs/AboutUs';
import './App.css';
import banner from './assets/banner.png';
import Contact from './Contact/Contact';
import Home from './Home/Home';
import PageNotFound from './PageNotFound/PageNotFound';
import { useAuth0 } from '@auth0/auth0-react';

export const browserHistory = createBrowserHistory({ basename: "/FrancaPaisa" });


function App() {
  const { loginWithRedirect, logout, isAuthenticated, user} = useAuth0();

  const styles = {
    styleIcons: {
      color: "blue"
    },
    styleContactInfo: {
      paddingBottom: 5
    },
    styleNavBar: {
      width: 20,
      marginTop: -5
    }
  }

  return (
    <div className="App">
      <header>
        <Router history={browserHistory} basename={'/FrancaPaisa'}>
          <img src={banner} className="App-logo " alt="logo" />
          <nav className="navbar-dark navbar-expand-sm navbar App-navbar sticky-top bg-dark" id="nav">
            <button className="navbar-toggler " type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span className="navbar-toggler-icon" ></span>
            </button>
            <div className="collapse navbar-collapse " id="navbarNav">

              <Nav.Link className="App-nav-link " href="/FrancaPaisa/">
                <AiOutlineHome style={styles.styleNavBar} /> Inmuebles
              </Nav.Link>
              <Nav.Link className="App-nav-link " href="/FrancaPaisa/about">
                <BsPeople style={styles.styleNavBar} /> Nosotros
              </Nav.Link>
              <Nav.Link className="App-nav-link " href="/FrancaPaisa/contact">
                <BiPhoneCall style={styles.styleNavBar} /> Contacto
              </Nav.Link>
              { 
                isAuthenticated ? (
                  <>
                    <Nav.Link className="App-nav-link" onClick={logout}>
                      <AiOutlineLogout style={styles.styleNavBar} /> {user.name}
                    </Nav.Link>
                  </>) : (<Nav.Link className="App-nav-link " onClick={loginWithRedirect}>
                    <AiOutlineUser style={styles.styleNavBar} /> Iniciar Sesión
                  </Nav.Link>)
              }

            </div>

          </nav>
          <Switch>
            <Route exact path="/" component={Home} />
            <Route exact path="/about" component={AboutUs} />
            <Route exact path="/contact" component={Contact} />
            <Route component={PageNotFound} />
          </Switch>

        </Router>
        <br></br>
      </header>
      <footer className="App-footer">
        <div className="row justify-content-center">
          <div className="col-md-auto" style={styles.styleContactInfo}>
            <h5><GoLocation style={styles.styleIcons} /> Calle 51 #52-09</h5>
          </div>
          <div className="col-md-auto" style={styles.styleContactInfo}>
            <h5><BiPhoneCall style={styles.styleIcons} /> +57 301123456</h5>
          </div>
          <div className="col-md-auto" style={styles.styleContactInfo}>
            <h5><AiOutlineQuestionCircle style={styles.styleIcons} /> ¿Dudas quejas o reclamos? <a href="/FrancaPaisa/contact">Contactenos</a></h5>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
