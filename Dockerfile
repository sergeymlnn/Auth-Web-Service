FROM python:3.9-slim as builder

COPY requirements.txt /

RUN pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt


FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=builder /wheels /wheels

WORKDIR /app
COPY app .

RUN addgroup --system app && \
    adduser --system --group app && \
    pip install --no-cache /wheels/* && \
    rm -rf /wheels /tmp
USER app
