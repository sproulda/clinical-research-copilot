# ---- Fixed Single-Stage Dockerfile ----
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies system-wide
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user and switch
RUN useradd -m appuser
USER appuser

# Expose FastAPI port
EXPOSE 8000

# Run app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]