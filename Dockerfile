FROM python:3.8.3

# Create app directory
WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv

RUN pip install -r /app/requirements.txt

EXPOSE 8000
CMD [ "python", "/app/api/api.py" ]