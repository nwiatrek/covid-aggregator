FROM python:3
WORKDIR /tmp
COPY . /tmp
RUN apt-get update
RUN pip install -r requirements.txt
CMD python -m pytest --cov=. --junitxml results.xml tests/
