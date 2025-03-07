import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  preview: {
    host: '0.0.0.0',
    port: process.env.PORT || 7000, // Usa el puerto asignado por Render
    allowedHosts: ['rna-risk-model-frontend.onrender.com'] // Agrega tu dominio de Render
  },
  server: {
    host: 'localhost',
    port: 7000,
    open: true, // Abre el navegador automáticamente
  },
  define: {
    'process.env': process.env
  },
});
