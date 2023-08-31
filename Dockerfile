
FROM python:3.9.2-slim-buster
RUN mkdir /bot && chmod 777 /bot
WORKDIR /bot
RUN apt-get -qq update && apt-get -qq install -y git wget pv jq ffmpeg mediainfo # Changed 'apt' to 'apt-get' for compatibility
RUN python -m pip install --upgrade pip
COPY . .
EXPOSE 8080
RUN pip install -r requirements.txt # Changed 'pip3' to 'pip' since 'pip' is the default package manager for Python 3.x
RUN apt-get -qq install -y procps # Added 'apt-get' command to install 'procps' package for 'healthcheck'
HEALTHCHECK --interval=5m --timeout=3s CMD ps aux | grep python || exit 1 # Added a health check command to check if python process is running
CMD ["bash", "run.sh"]
