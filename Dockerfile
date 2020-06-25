FROM python:3.8.3

# Create app directory
WORKDIR /app

# Install app dependencies
COPY ./requirements.txt /app/requirements.txt
COPY ./daniscarpa-venv /app/venv

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv
RUN /bin/bash -c "source /app/venv/bin/activate"
RUN pip install -r /app/requirements.txt


# Bundle app source
COPY api /app/api
COPY models /app/models
COPY resources /app/resources
COPY schemas /app/schemas

EXPOSE 8080
CMD [ "python", "app/api.py" ]
