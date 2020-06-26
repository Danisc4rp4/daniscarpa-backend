FROM python:3.8.3

COPY . /app
WORKDIR /app

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 && pip install -r ./requirements.txt

EXPOSE 8000
CMD [ "flask", "run" ]