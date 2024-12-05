FROM python:3.9-slim
RUN pip install flask
COPY . .
WORKDIR /app
CMD ["python", "main.py"]
