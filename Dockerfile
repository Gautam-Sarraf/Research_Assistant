FROM python:3.10-slim

WORKDIR /app

# Copy dependency definition
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code from the current directory context
COPY . .

# Expose port (default 8000)
EXPOSE 8000

# Set environment variables
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

# Run uvicorn server (main:app since main.py is copied to /app)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port $PORT"]
