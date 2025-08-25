# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install git (if you want to fetch Exercism problems inside container)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Copy your repo files into container
COPY . .

# Optional: install dependencies (if you need requests, pytest, etc.)
# RUN pip install -r requirements.txt

# Default command (start a Python REPL)
CMD ["python3"]
