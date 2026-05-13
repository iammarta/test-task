FROM python:3.11.15-slim
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY parser.py .
ENTRYPOINT ["python", "parser.py"]