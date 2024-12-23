# FROM python:3.8.12-slim
FROM python:3.10-slim

RUN pip install pipenv

# Create working directory in docker image
WORKDIR /app

# Copy Pipfile and Pipfile.lock files in working dir
COPY ["Pipfile", "Pipfile.lock", "./"]

# Install required packages using pipenv
RUN pipenv install --system --deploy

# Copy gateway and protobuf scripts in the working dir
COPY ["gateway.py", "proto.py", "./"]

EXPOSE 9696


ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "--timeout=120", "gateway:app"]