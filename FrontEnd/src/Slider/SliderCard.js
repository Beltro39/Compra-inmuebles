import './Slider.css';

const SliderCard = props => {

    return (
        <div className="form-group">
            <div className="row no-gutters">

                <div className="col-8 ">
                    <img className="card-img-slider" src={props.img} alt="Card slider" />
                </div>

                <div className="col-4">
                    <div className="bg-dark label-slider-container">
                        <p className="text-align-center"><strong>Recomendado</strong></p>
                        <p className="text-align-left"><strong>Lugar:</strong> {props.lugar}</p>
                        <p className="text-align-left"><strong>Tipo:</strong> {props.tipo}</p>
                        <p className="text-align-left"><strong>Precio:</strong> {props.precio}</p>
                        <p className="text-align-left"><strong>Fuente:</strong> {props.fuente}</p>
                        <a href={props.url} target="_blank" rel="noreferrer" className="btn btn-primary button">Más información</a>

                    </div>
                </div> 

                
            </div>
        </div>
    )
  }

export default SliderCard;