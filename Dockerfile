FROM python:3.6-slim

WORKDIR /usr/src/

COPY ./application/app ./app
ADD ./application/requirements.txt .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install waitress

RUN rm requirements.txt

ADD ./application/startup.sh .
RUN chmod +x ./startup.sh

VOLUME /usr/src/instance
EXPOSE 8080

ENTRYPOINT ["./startup.sh"]