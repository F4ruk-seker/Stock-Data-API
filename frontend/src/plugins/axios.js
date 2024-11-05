import axios from 'axios';


const instance = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL || 'https://api.example.com',
});

// İstek interceptor'ı: Her istekte yapılacak işlemler
instance.interceptors.request.use(
    (config) => {
      console.log(`İstek yapılıyor: ${config.url}`);
      const token = localStorage.getItem('token');
      if (token) {
        config.headers.Authorization = `Bearer ${token}`;
      }
      return config;
    },
    (error) => Promise.reject(error)
  );
  
  // Yanıt interceptor'ı: Her yanıtta yapılacak işlemler
  instance.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response && error.response.status === 401) {
        // Örneğin, 401 durumunda giriş sayfasına yönlendirme
        window.location.href = '/login';
      }
      return Promise.reject(error);
    }
  );
  
  export default instance;