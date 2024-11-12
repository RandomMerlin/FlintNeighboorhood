# Stage 1: Build the Vite app
FROM node:18-alpine AS build

# Set working directory
WORKDIR /app

# Install dependencies separately to leverage Docker caching
COPY package*.json ./
RUN npm install --frozen-lockfile

# Copy the rest of the application code
COPY . .

# Build the app for production
RUN npm run build

# Stage 2: Serve the built app with a lightweight web server
FROM nginx:alpine

# Copy the built app from the previous stage to the nginx web directory
COPY --from=build /app/dist /usr/share/nginx/html

# Expose the port that the app will run on
EXPOSE 8080

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
