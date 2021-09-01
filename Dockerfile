FROM python:3.8-alpine
COPY ["app", "requirements.txt", "./"]
RUN pip install fastapi uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
