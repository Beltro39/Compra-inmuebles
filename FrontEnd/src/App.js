import banner from './assets/banner.png';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import { GoLocation } from 'react-icons/go';
import { BiPhoneCall } from 'react-icons/bi';
import { BsPeople } from 'react-icons/bs';
import {
  AiOutlineQuestionCircle,
  AiOutlineHome,
  AiOutlineUser
} from 'react-icons/ai';
import AboutUs from './AboutUs/AboutUs';
import Contact from './Contact/Contact';
import Home from './Home/Home';
import PageNotFound from './PageNotFound/PageNotFound';
import Login from './Login/Login';
import Register from './Register/Register';

import { createBrowserHistory } from 'history';
export const browserHistory = createBrowserHistory({basename : "/FrancaPaisa"});

function App() {


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
      <header className="App-header">
        <Router history={browserHistory} basename = {'/FrancaPaisa'}>
          <div>
            <img src={banner} className="App-logo" alt="logo" />
            <Navbar className="App-navbar justify-content-center" bg="dark" variant="dark" sticky="top">
              <Nav.Link className="App-nav-link" href="/FrancaPaisa/">
                <AiOutlineHome style={styles.styleNavBar} /> Inmuebles
              </Nav.Link>
              <Nav.Link className="App-nav-link" href="/FrancaPaisa/about">
                <BsPeople style={styles.styleNavBar} /> Nosotros
              </Nav.Link>
              <Nav.Link className="App-nav-link" href="/FrancaPaisa/contact">
                <BiPhoneCall style={styles.styleNavBar} /> Contacto
              </Nav.Link>
              <Nav.Link className="App-nav-link" href="/FrancaPaisa/login">
                <AiOutlineUser style={styles.styleNavBar} /> Iniciar Sesión
              </Nav.Link>
            </Navbar>
            <Switch>
              <Route exact path="/" component={Home} />
              <Route exact path="/about" component={AboutUs} />
              <Route exact path="/contact" component={Contact} />
              <Route exact path="/login" component={Login} />
              <Route exact path="/register" component={Register} />
              <Route component={PageNotFound} />
            </Switch>
          </div>
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
            <h5><AiOutlineQuestionCircle style={styles.styleIcons} /> ¿Dudas quejas o reclamos? <a href = "/FrancaPaisa/contact">Contactenos</a></h5>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;
