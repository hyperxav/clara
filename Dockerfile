# Use Python 3.10 slim image as base
FROM python:3.10-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code files
COPY . .

# Set the default command
CMD ["python", "clara_bot.py"] 