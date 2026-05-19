// Configuración para producción.
// Apunta al backend Flask desplegado en Render Cloud.
//
// URL del backend: https://foodplease-api-grupo03.onrender.com
// (servicio web gratuito de Render, despliegue automático desde GitHub).

export const environment = {
  production: true,
  apiUrl: 'https://foodplease-api-grupo03.onrender.com/api/v1',
  appName: 'FoodPlease',
  appVersion: '1.0.0',
};
