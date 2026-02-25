# ---- Single-Stage Python App Dockerfile ----
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies system-wide
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create non-root user and switch
RUN useradd -m appuser
USER appuser

# Expose port for FastAPI
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]