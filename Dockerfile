FROM ubuntu:20.04

RUN apt-get update -y && apt-get install && apt-get upgrade -y python-pip python-dev libpq-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]