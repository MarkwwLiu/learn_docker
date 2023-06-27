FROM python:3.8

WORKDIR /
COPY ./requestment.txt /
COPY ./api.py /
RUN pip install -r requestment.txt


CMD ["python", "api.py"]
