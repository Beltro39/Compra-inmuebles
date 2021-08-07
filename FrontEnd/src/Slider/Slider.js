import './Slider.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';
import SliderCard from './SliderCard';
import houses from '../assets/casa.jpg';

function Slider() {

    return (

        <div id="mycarousel" class="carousel slide" data-ride="carousel">
            <div class="carousel-inner" role="listbox">
                <div class="carousel-item active">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>
                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>

                <div class="carousel-item ">
                    <SliderCard img={houses} lugar="Loma de los bernal" tipo="casa" precio="350'000.000" fuente="Fincaraiz.com" />
                </div>
            </div>
            <ol class="carousel-indicators">
                <li data-target="#mycarousel" data-slide-to="0" class="active"></li>
                <li data-target="#mycarousel" data-slide-to="1"></li>
                <li data-target="#mycarousel" data-slide-to="2"></li>
                <li data-target="#mycarousel" data-slide-to="3"></li>
                <li data-target="#mycarousel" data-slide-to="4"></li>
                <li data-target="#mycarousel" data-slide-to="5"></li>
                <li data-target="#mycarousel" data-slide-to="6"></li>
                <li data-target="#mycarousel" data-slide-to="7"></li>
                <li data-target="#mycarousel" data-slide-to="8"></li>
                <li data-target="#mycarousel" data-slide-to="9"></li>
            </ol>
            <a class="carousel-control-prev" href="#mycarousel" role="button" data-slide="prev">
                <span class="carousel-control-prev-icon"></span>
            </a>
            <a class="carousel-control-next" href="#mycarousel" role="button" data-slide="next">
                <span class="carousel-control-next-icon"></span>
            </a>


        </div>

    );
}

export default Slider;


