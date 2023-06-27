FROM python:3.8.16

ENV GRAFANA_TOKEN="glsa_IBdAezrDDpHqbQM8cKBw4OHt1WKnM8i3_0806515a"
ENV GRAFANA_DATASOURCE_URL="http://host.docker.internal:3000"

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "push-datasources.py" ]