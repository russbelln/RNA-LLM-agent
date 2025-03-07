# Usa una imagen base oficial de Node.js
# Usa una imagen base oficial de Node.js
FROM node:18-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /frontend

# Copia el resto del código fuente al contenedor
COPY . .

# Instala las dependencias
RUN npm install

# Construye la aplicación para producción
RUN npm run build

# Expone el puerto en el que la aplicación correrá
EXPOSE 7000

# Comando para correr la aplicación
CMD ["npm", "run", "preview"]
