FROM python:3.11

WORKDIR /usr/src/myapp

RUN apt-get update && apt-get install -qq -y nodejs npm

RUN curl https://files.stork-search.net/releases/v1.5.0/stork-ubuntu-20-04 -o stork \
    && chmod +x stork \
    && mv ./stork /usr/local/bin/stork

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN npm install -g sass
RUN npm install -g juice

# pelican setup
COPY content content
COPY plugins plugins
COPY themes themes
COPY pelicanconf.py pelicanconf.py

COPY publishing/*.sh ./
RUN chmod 777 *.sh

CMD ["pelican", "--delete-output-directory", "content"]
