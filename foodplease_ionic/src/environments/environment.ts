// Configuración para desarrollo local.
// Apunta al backend Flask corriendo en http://127.0.0.1:5000
//
// IMPORTANTE: cuando se ejecute `ionic serve` el frontend corre en localhost:8100
// y consume la API REST del backend Flask en localhost:5000. CORS ya está
// habilitado en el backend (Flask-CORS) para aceptar requests desde cualquier origen.

export const environment = {
  production: false,
  apiUrl: 'http://127.0.0.1:5000/api/v1',
  appName: 'FoodPlease',
  appVersion: '1.0.0',
};
