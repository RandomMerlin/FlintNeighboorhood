# Step 1: Use a Node.js image as the base
FROM node:18 AS build

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy package.json and package-lock.json, then install dependencies
COPY package*.json ./
RUN npm install

# Step 4: Copy the rest of the application code
COPY . .

# Step 5: Build the Vite React app
RUN npm run build

# Step 6: Use a lightweight web server to serve the app (e.g., nginx)
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 3000

# Start nginx server
CMD ["nginx", "-g", "daemon off;"]
