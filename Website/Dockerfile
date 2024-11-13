# Step 1: Use Node.js image for building the app
FROM node:18 AS build

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json, and install dependencies
COPY package*.json ./
RUN npm install

# Copy the application source code
COPY . .

# Build the Vite React app
RUN npm run build

# Step 2: Serve the app with Node.js
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the build output from the previous stage
COPY --from=build /app/dist /app/dist

# Install an HTTP server for serving static files
RUN npm install -g serve

# Set environment variables for Cloud Run
ENV PORT=8080

# Expose the Cloud Run port
EXPOSE 8080

# Command to serve the static files
CMD ["serve", "-s", "dist", "-l", "8080"]
