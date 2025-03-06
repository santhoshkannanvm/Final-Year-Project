import requests

# Send a GET request
response = requests.get('https://api.example.com/resource')

# Check the response status code
if response.status_code == 200:
    # Request successful
    data = response.json()  # Assuming the response is in JSON format
    # Process the data
    print(data)
else:
    # Request failed
    print('Error:', response.status_code)
