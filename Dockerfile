FROM slim

ENV PYTHONWRITEBYTHCODE=1 PYTHONBUFFERED=1

WORKDIR /usr/app

ADD . /app

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

USER appuser

CMD "python main.py"