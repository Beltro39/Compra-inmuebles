//function Cards(props){
//    return 
//}

const Listcards = props => {
    return (
        <div class="card form-group">
            <div class="row no-gutters">
                <div className="col-sm">
                    <img class="card-img-top" src={props.img} alt="Card cap" />
                </div>

                <div class="col-sm">
                    <div class="card-body bg-dark">
                        <p class="card-text text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                        <p class="card-text text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                        <p class="card-text text-align-left"><strong>Precio:</strong> {props.precio}</p>
                        <p class="card-text text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                    </div>
                </div>

                <div class="col-sm center bg-dark">
                    <a href="/" class="btn btn-primary button">Más información</a>
                </div>
            </div>
        </div>
    )
  }

export default Listcards; 