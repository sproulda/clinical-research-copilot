# ---- Fixed Single-Stage Dockerfile ----
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies system-wide
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir 'uvicorn[standard]' 'fastapi' 'pydantic-settings'

# Copy the **entire project**, including populate_db.py
COPY . .

# Create non-root user and switch
RUN useradd -m appuser
USER appuser

# Ensure user-local and system bin dirs are on PATH
ENV PATH="/home/appuser/.local/bin:/usr/local/bin:$PATH"

# Expose FastAPI port
EXPOSE 8000

# Run app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]