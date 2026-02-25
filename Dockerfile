# ---- Build Stage ----
FROM python:3.9-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Final Stage ----
FROM python:3.9-slim

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local

# Copy application code
COPY . .

USER appuser

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]