# Docker Support for Mentora

This directory contains Docker configuration for containerizing the Mentora application.

## Files

- `Dockerfile` - Container definition for the Flask application
- `docker-compose.yml` - Multi-container orchestration (Flask + MongoDB)

## Quick Start with Docker

### Prerequisites
- Docker
- Docker Compose

### Build and Run

```bash
# Build and start containers
docker-compose up --build

# Access application
# Flask app: http://localhost:5000
# MongoDB: localhost:27017
```

### Stop Containers

```bash
docker-compose down
```

## Services

- **web**: Flask application running on port 5000
- **mongo**: MongoDB database on port 27017

## Environment

Edit `.env` file or set environment variables:
- `MONGO_URI`: MongoDB connection string
- `SECRET_KEY`: Flask secret key
- `GOOGLE_API_KEY`: Google API key for AI features

## Volumes

- `mongo_data`: Persistent MongoDB data volume

## Logs

```bash
# View logs
docker-compose logs -f web

# View specific service logs
docker-compose logs -f mongo
```

See Dockerfile and docker-compose.yml for detailed configuration.
