FROM python:3.9-slim
RUN pip install -r requirements.txt
COPY . .
WORKDIR /app
CMD ["python", "main.py"]
