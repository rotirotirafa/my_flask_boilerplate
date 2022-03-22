FROM ubuntu:20.04

RUN apt-get update -y && apt-get install && apt-get upgrade -y python-dev libpq-dev python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r /app/requirements.txt

COPY . .

CMD [ "flask init" ]

# Apenas manter flask upgrade para casos de deploy.
CMD [ "flask migrate" ]

CMD [ "flask upgrade"]

ENTRYPOINT [ "python3" ]

CMD [ "wsgi.py" ]