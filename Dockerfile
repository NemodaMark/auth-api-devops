# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set work directory inside the container
WORKDIR /app

# Install OS-level dependencies (optional but useful for many Python packages)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your app listens on
EXPOSE 8080

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV FLASK_ENV=production

# Run the app
CMD ["python", "-m", "app.main"]
