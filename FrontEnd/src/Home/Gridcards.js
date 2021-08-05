
const Gridcards = props => {
    return (
        <div class="col-sm-4">
            <div class="card">
                <img class="card-img-top" src={props.img} alt="Card image cap"/>
                <div class="card-body bg-dark">
                    <p class="card-text text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                    <p class="card-text text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                    <p class="card-text text-align-left"><strong>Precio:</strong> {props.precio}</p>
                    <p class="card-text text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                    <a href="#" class="btn btn-primary">Más información</a>
                </div>
            </div>
            <br></br>
        </div>
        
    )
  }

  export default Gridcards;