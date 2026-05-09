# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.14-alpine

ENV APP_HOME=/app
WORKDIR $APP_HOME

RUN apk add --update --no-cache git

# Copy local code to the container image.
# Install production dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./

# Add credentials
RUN set GOOGLE_APPLICATION_CREDENTIALS="google-authorisation.json"
EXPOSE 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app
