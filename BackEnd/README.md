# Información del sistema


## Lista de paquetes necesarios con su respectiva versión

- Pyhon 3.9  *Documentation: https://docs.python.org/3/*
- Django 3.2  *Documentation: https://docs.djangoproject.com/en/3.2/*
- PostgreSQL 13.2  *Documentation: https://www.postgresql.org/docs/13/index.html*

### Instalación base de datos.

    pacman -S postgresql-13
    su - postgres
    initdb -D /var/lib/postgres/data

### Información bases de datos:

Base de datos de almacenamiento de resultados del web scrapping.

    fp_scrapping
    USER "FrancaPaisa"
    PASSWORD 'FP#$tS'
    
## Consumo de servicios 

### Scrapping List Service Paginated Data

GET /FrancaPaisa-Servicios/v0/francapaisa-inmuebles/scrapping/?pageSize=300&pageNumber=1

### Scrapping List By Filter Service Paginated Data

GET /FrancaPaisa-Servicios/v0/francapaisa-inmuebles/scrapping-filtro/?pageSize=300&pageNumber=1

### Tipo Inmueble List Service Data

GET /FrancaPaisa-Servicios/v0/francapaisa-inmuebles/tipo-inmueble/

### Scrapping List Service Paginated Data

GET /FrancaPaisa-Servicios/v0/francapaisa-inmuebles/scrapping/

# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory, you can run:

### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

### `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

### Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

### Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

### Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

### Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)

