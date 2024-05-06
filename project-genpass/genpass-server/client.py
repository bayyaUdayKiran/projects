# This program isn't a functional part of the project and is only to guide users to manage the server..
import requests

# Get data
response = requests.get('http://127.0.0.1:5000/get_data')
print(response.json())

# Write data
new_data = {'key': 'value'}
response = requests.post('http://127.0.0.1:5000/write_data', json=new_data)
print(response.json())
