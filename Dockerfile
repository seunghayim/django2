FROM python:3.8.10

COPY . /app
WORKDIR /app

RUN apt-get update
RUN yes | apt-get install python3-dev default-libmysqlclient-dev build-essential

RUN python3 -m venv /opt/venv && sh /opt/venv/bin/activate

RUN pip install pip --upgrade && pip install -r requirements.txt && chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]