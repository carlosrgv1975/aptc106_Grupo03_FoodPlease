// Configuración para producción (despliegue Cloud en Render).
// La URL se actualizará cuando el backend Flask esté desplegado.

export const environment = {
  production: true,
  apiUrl: 'https://foodplease-api.onrender.com/api/v1',  // pendiente de actualizar tras deploy
  appName: 'FoodPlease',
  appVersion: '1.0.0',
};
