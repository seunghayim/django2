FROM python:3.8.3-slim

COPY . /app

WORKDIR /app

RUN apt-get update
RUN yes | apt-get install python3-dev default-libmysqlclient-dev build-essential

RUN python3 -m venv /opt/venv

RUN /opt/venv/bin/pip install pip --upgrade && \
  /opt/venv/bin/pip install -r requirements.txt && \
  chmod +x entrypoint.sh && chmod +x migrate.sh && chmod +x collectstatic.sh

CMD [ "/app/entrypoint.sh" ]