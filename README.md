# Grafana Datasource Creation

This repository contains a Python script that reads a JSON file and makes API calls to create datasources in Grafana. The script is designed to handle datasources one by one, with a delay between each API call to avoid overwhelming Grafana.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.8 or later
- Pip package manager

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/GPegel/grafana-datasource-creation.git

2. Navigate to the repository directory:

    ```bash
    cd grafana-datasource-creation

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt

## Usage

1. Edit the data.json file and add your desired datasources in the JSON format.
2. Set the necessary environment variables:
2. GRAFANA_TOKEN: Your Grafana authentication token.
2. GRAFANA_DATASOURCE_URL: The URL of your Grafana datasource endpoint.
3. Run the Python script:

    ```bash
    python push-datasources.py

4. Or if you want to run this script in a docker container, you can use the following command:

    ```bash
    docker run -it --rm -e GRAFANA_TOKEN=your-token -e GRAFANA_DATASOURCE_URL=your-url -v $(pwd)/data.json:/app/data.json ghcr.io/your-username/grafana-datasource-creation:latest
