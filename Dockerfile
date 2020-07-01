FROM python:3.8.3

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 && pip install -r ./requirements.txt

EXPOSE 5000
CMD [ "flask", "run", "--host=0.0.0.0"]