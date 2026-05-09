# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Get system dependencies
RUN set -e; \
    apt-get update -y && apt-get install -y \
    tini \
    gnupg \
    curl \
    lsb-release; \
    gcsFuseRepo=gcsfuse-`lsb_release -c -s`; \
    echo "deb http://packages.cloud.google.com/apt $gcsFuseRepo main" | \
    tee /etc/apt/sources.list.d/gcsfuse.list; \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | \
    apt-key add -; \
    # Now with gcsfuse added to repos
    apt-get update -y && apt-get install -y \
    libmagic-dev \
    ffmpeg \
    gcsfuse \
    && apt-get clean

# Set mount directory
ENV MNT_DIR=/mnt/content
ENV BUCKET=addlyrics-content
ENV APP_HOME=/app
WORKDIR $APP_HOME

# Ensure the startup script is executable

# Install production dependencies.
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./
RUN chmod +x /app/run.sh

# Add credentials
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/google-authorisation.json"
EXPOSE 8080
ENV PORT=8080

ENTRYPOINT ["/usr/bin/tini", "--"] 

CMD ["/app/run.sh"]
