FROM python:3.14.0a3

RUN mkdir -p /usr/src/app
COPY ./ /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirement.txt

ENV PROD=True
ENV FLASK_ENV=production

CMD ["python3", "src/app.py"]