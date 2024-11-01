FROM python:3.12.7-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /djangoblog

WORKDIR /djangoblog

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]