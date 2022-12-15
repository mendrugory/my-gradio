FROM python:3.10.6-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./*.py ./

ENTRYPOINT ["python", "main.py"]