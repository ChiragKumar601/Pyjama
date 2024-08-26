# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set the working directory in the container
WORKDIR /app

RUN mkdir -p /app/logs

# Set permissions
RUN chown -R www-data:www-data /app/logs

# Install supervisor
RUN apt-get update && \
    apt-get install -y supervisor && \
    rm -rf /var/lib/apt/lists/*

# Install PostgreSQL development dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code to /app
COPY . /app/

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 8000 to allow external access to the server
EXPOSE 8000

CMD ["supervisord"]