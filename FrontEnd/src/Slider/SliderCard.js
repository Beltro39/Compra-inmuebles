import './Slider.css';

const SliderCard = props => {

    return (
        <div class="form-group">
            <div class="row no-gutters">

                <div className="col-8 ">
                    <img class="card-img-slider" src={props.img} alt="Card image cap" />
                </div>

                <div class="col-4">
                    <div class="bg-dark label-slider-container">
                        <p class="text-align-center"><strong>Recomendado</strong></p>
                        <p class="text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                        <p class="text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                        <p class="text-align-left"><strong>Precio:</strong> {props.precio}</p>
                        <p class="text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                        <a href="#" class="btn btn-primary button">Más información</a>

                    </div>
                </div>

                
            </div>
        </div>
    )
  }

export default SliderCard;