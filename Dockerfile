FROM python:3.10-slim

WORKDIR /app

# Copy dependency definition from root
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY research_assistant/ ./research_assistant/

# Expose port (default 8000, can be overridden by environment variable)
EXPOSE 8000

# Set environment variables
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

# Run uvicorn server
CMD ["sh", "-c", "uvicorn research_assistant.main:app --host 0.0.0.0 --port $PORT"]
