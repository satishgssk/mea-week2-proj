FROM python:latest

WORKDIR /app

COPY . .

ARG PORT=8080

RUN pip install -r "requirements.txt"

EXPOSE ${PORT}

ENTRYPOINT ["python", "lbg.py"]
