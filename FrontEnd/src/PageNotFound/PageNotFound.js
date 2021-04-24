import './PageNotFound.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import notFoundImage from '../assets/pageNotFound.png';

function PageNotFound() {
    return (
        <div className="PageNotFound">
            <header className="PageNotFound-header">
                <img src={notFoundImage} className="PageNotFound" alt="logo" />
            </header>
        </div>
    );
}

export default PageNotFound;
