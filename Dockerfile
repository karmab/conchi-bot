FROM gliderlabs/alpine:3.6
MAINTAINER Karim Boumedhel <karimboumedhel@gmail.com>

RUN apk add --no-cache python python-dev py-pip build-base \
  && pip install PyTelegramBotAPI emoji

ADD conchibot.py /

CMD ["python", "-u", "/conchibot.py"]
