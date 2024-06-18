FROM python:3.12-slim
WORKDIR /app

COPY pyproject.toml .
COPY requirements.lock .
RUN pip install --no-cache-dir -r requirements.lock

COPY contract_extractor/ .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
