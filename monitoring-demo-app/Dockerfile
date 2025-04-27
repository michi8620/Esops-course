FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create templates directory if not exists
RUN mkdir -p templates

# Set environment variables
ENV PORT=8080
ENV PYTHONUNBUFFERED=1

# Expose the port the app will run on
EXPOSE 8080

# Command to run the application
CMD ["python", "main.py"]