//function Cards(props){
//    return 
//}

const Listcards = props => {
    return (
        <div className="card form-group">
            <div className="row no-gutters">
                <div className="col-sm">
                    <img className="card-img-top" src={props.img} alt="Card cap" />
                </div>

                <div className="col-sm">
                    <div className="card-body bg-dark">
                        <p className="card-text text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                        <p className="card-text text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                        <p className="card-text text-align-left"><strong>Precio:</strong> {props.precio}</p>
                        <p className="card-text text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                    </div>
                </div>

                <div className="col-sm center bg-dark">
                    <a href="/" className="btn btn-primary button">Más información</a>
                </div>
            </div>
        </div>
    )
  }

export default Listcards; 