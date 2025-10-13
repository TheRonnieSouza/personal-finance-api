# Use Python 3.12 slim image for smaller container size
# Slim version reduces image size by excluding unnecessary packages
FROM python:3.12-slim

# Set environment variables for Python optimization
# PYTHONUNBUFFERED=1: Ensures Python output is sent straight to terminal without buffering
# PYTHONDONTWRITEBYTECODE=1: Prevents Python from writing .pyc files to disk
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install system dependencies (minimal for FastAPI + PostgreSQL)
# gcc: Required for compiling Python packages
# libpq-dev: PostgreSQL development libraries for psycopg2
# Clean up apt cache after installation to reduce image size
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
# All subsequent commands will be run from this directory
WORKDIR /app

# Copy Poetry configuration files
# These files define project dependencies and their versions
COPY pyproject.toml poetry.lock ./

# Install dependencies directly with pip instead of using Poetry virtual environment
# This ensures all packages are available system-wide including database drivers
RUN pip install fastapi uvicorn python-dotenv sqlalchemy psycopg2-binary

# Copy application source code and environment file
# src/ contains the FastAPI application
COPY src/ ./src/
COPY .env ./

# Create a non-root user for security best practices
# Running containers as root can be a security risk
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app

# Switch to non-root user
USER appuser

# Expose port 8000 to allow external access
# This is the port where FastAPI/Uvicorn will listen for requests
EXPOSE 8000

# Start the FastAPI application using Python directly
# This runs the uvicorn server from within the Python script
CMD ["python", "src/financial_manager/main.py"]
