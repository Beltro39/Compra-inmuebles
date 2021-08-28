import './Home.css';

const Gridcards = props => {
    return (
        <div className="col-sm-4">
            <div className="card" style={{marginBottom:"20px"}}>
                <img className="card-img-top card-img-top-grid" src={props.img} alt="Card cap"/>
                <div className="card-body bg-dark">
                    <p className="card-text text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                    <p className="card-text text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                    <p className="card-text text-align-left"><strong>Precio:</strong> {props.precio}</p>
                    <p className="card-text text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                    <a href={props.url} className="btn btn-primary" target="_blank" rel="noreferrer">Más información</a>
                </div>
            </div>
        </div>
    )
  }

  export default Gridcards;