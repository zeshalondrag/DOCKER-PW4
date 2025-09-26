FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

ENV DISPLAY=host.docker.internal:0

WORKDIR /app
COPY calculator.py .

CMD ["python3", "calculator.py"]