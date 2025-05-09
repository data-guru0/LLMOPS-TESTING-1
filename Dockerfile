# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy entire project
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -e .


# Expose port for Streamlit and FastAPI
EXPOSE 8501
EXPOSE 9999

CMD ["python", "app/main.py"]
