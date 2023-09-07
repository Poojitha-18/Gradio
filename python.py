import requests

# Define the skills to search for
skills_to_search = "Python,Java"

# API endpoint
url = "http://localhost:5000/search"

# Define the parameters for the GET request
params = {'skills': skills_to_search}

# Send a GET request to the API
response = requests.get(url, params=params)

# If the request was successful, print the data
if response.status_code == 200:
    users = response.json()
    for user in users:
        print(f"{user['first_name']} {user['last_name']} has skill {user['skill']}")
else:
    print(f"Error: Received status code {response.status_code} from server")