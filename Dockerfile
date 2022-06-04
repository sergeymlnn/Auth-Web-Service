FROM python:3.9-slim as builder

# LABEL stage=builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY app/requirements.txt .

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /wheels /wheels
COPY ./app /app

RUN addgroup --system app && \
    adduser --system --group app && \
    pip install --no-cache /wheels/* && \
    rm -rf /wheels /tmp && \
    rm requirements.txt
USER app
