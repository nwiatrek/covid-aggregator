FROM python:3
WORKDIR /tmp
COPY . /tmp
RUN apt-get update
RUN pip install -r covid-aggregator/requirements.txt
RUN touch covid-aggregator/tests/results.xml
CMD python -m pytest --cov=. --junitxml results.xml covid-aggregator/tests/
