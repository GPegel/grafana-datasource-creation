import os
import json
import requests
import time

# Get the bearer token from an environment variable
token = os.environ.get('GRAFANA_TOKEN')

# Ensure the token is available
if not token:
    raise ValueError('Grafana token not found in environment variable.')

# Get the Grafana datasource URL from an environment variable
datasource_url = os.environ.get('GRAFANA_DATASOURCE_URL')

# Ensure the datasource URL is available
if not datasource_url:
    raise ValueError('Grafana datasource URL not found in environment variable.')

# Grafana API endpoint and authentication details
url = f'{datasource_url}/api/datasources'
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}

# Read the JSON file
with open('example_datasources.json') as file:
    datasources = json.load(file)

# Iterate over the datasources and make API calls
for datasource in datasources:
    response = requests.post(url, headers=headers, json=datasource)
    
    if response.status_code == 200:
        print('Datasource created successfully:', datasource['name'])
    else:
        print('Failed to create the datasource:', datasource['name'])
    
    # Print the API response
    print(response.text)
    
    # Add a delay between each API call (adjust the delay time as needed)
    time.sleep(1)
