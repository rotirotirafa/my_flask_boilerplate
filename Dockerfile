FROM ubuntu:18.04

RUN apt-get update -y && apt-get install -y python-pip python-dev libpq-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 8000

ENTRYPOINT [ "python" ]

CMD [ "run.py" ]