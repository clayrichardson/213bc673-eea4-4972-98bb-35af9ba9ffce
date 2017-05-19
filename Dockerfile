FROM python:3.5

RUN apt-get update && apt-get install -y python-setuptools \
python-dev \
libffi-dev \
libssl-dev \
jq

ADD ./requirements.txt /opt/lib/requirements.txt
RUN cd /opt/lib/ && pip install -r ./requirements.txt

WORKDIR /opt/python
