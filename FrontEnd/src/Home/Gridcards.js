
const Gridcards = props => {
    return (
        <div className="col-sm-4">
            <div className="card">
                <img className="card-img-top" src={props.img} alt="Card cap"/>
                <div className="card-body bg-dark">
                    <p className="card-text text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                    <p className="card-text text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                    <p className="card-text text-align-left"><strong>Precio:</strong> {props.precio}</p>
                    <p className="card-text text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                    <a href="/" className="btn btn-primary">Más información</a>
                </div>
            </div>
            <br></br>
        </div>
        
    )
  }

  export default Gridcards;