FROM python:3.6

WORKDIR /code
ADD . /code

ADD requirements.txt requirements.txt
ADD requirements.in requirements.int
RUN pip install --upgrade pip
RUN pip install pip-tools
RUN pip-compile --output-file requirements.txt requirements.in

RUN pip install -r requirements.txt

CMD ["python", "producer.py"]