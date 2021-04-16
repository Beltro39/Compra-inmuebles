import banner from './assets/banner.png';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Navbar, Nav } from 'react-bootstrap';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import AboutUs from './AboutUs';
import Contact from './Contact';
import Home from './Home';
import PageNotFound from './PageNotFound';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Router>
          <div>
            <img src={banner} className="App-logo" alt="logo" />
            <Navbar className="App-navbar justify-content-center" bg="dark" variant="dark" sticky="top">
              <Nav.Link className="App-nav-link" href="/">Inmuebles</Nav.Link>
              <Nav.Link className="App-nav-link" href="/about">Nosotros</Nav.Link>
              <Nav.Link className="App-nav-link" href="/contact">Contacto</Nav.Link>
            </Navbar>
            <Switch>
              <Route exact path="/" component={Home} />
              <Route exact path="/about" component={AboutUs} />
              <Route exact path="/contact" component={Contact} />
              <Route component={PageNotFound} />
            </Switch>
          </div>
        </Router>
      </header>
    </div>
  );
}

export default App;
