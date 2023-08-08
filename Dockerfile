FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt install -y libpq-dev

RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/

WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv

# Copy the Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy the project files to the container
COPY . /code/

ENV HOME=/home/python
ENV APP_HOME=/home/python/app

RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

CMD ["pipenv", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]