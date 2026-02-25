# ---- Builder Stage ----
FROM python:3.9-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# ---- Final Stage ----
FROM python:3.9-slim
WORKDIR /app
RUN useradd -m appuser
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app
USER appuser
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]