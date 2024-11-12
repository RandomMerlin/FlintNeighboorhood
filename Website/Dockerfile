# Stage 1: Build the Vite app
FROM node:18-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the package files and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app files and build the app
COPY . .
RUN npm run build

# Stage 2: Serve the app with a lightweight server
FROM node:18-slim

# Install the serve package globally
RUN npm install -g serve

# Copy the built files from the previous stage
COPY --from=builder /app/dist /app

# Set the default command to serve the app on port 8080
EXPOSE 8080
CMD ["serve", "-s", "/app", "-l", "8080"]
