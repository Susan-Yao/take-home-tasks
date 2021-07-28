FROM python:3.7.5-slim

RUN apt-get update -y && apt-get install -y python-pip python-dev
RUN apt-get update && apt-get install -y python3.7 python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5000
EXPOSE 587

ENTRYPOINT [ "python", "app.py" ]