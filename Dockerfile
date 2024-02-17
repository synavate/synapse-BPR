# Use official Python image with slim variant
FROM python:3.9-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VERSION=1.1.10

# Install system dependencies
RUN apt-get update \
    && apt-get install --no-install-recommends -y \
       build-essential \
       curl \
       git \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set working directory
WORKDIR /app

# Copy only dependencies to cache them in Docker layer
COPY poetry.lock pyproject.toml ./

# Install project dependencies
RUN poetry install --no-root --no-dev

# Production image
FROM base AS production

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
