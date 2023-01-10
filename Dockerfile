# Pull base image
FROM python:3.11.1-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /school

# Install dependencies
COPY Pipfile Pipfile.lock /school/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /school/
