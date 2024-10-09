import requests

# URL of the API endpoint
url = "https://staging-sp.api.achievetestprep.com/api/v1/employees/bypass"

# Data to be sent in the POST request
data = {
    "employee_email": "atp.dev.adm1n01@gmail.com",
    "secret": "@ATP!tester$001"
}

# Sending POST request
response = requests.post(url, json=data)  # Sending JSON data

# Checking the status code of the response
if response.status_code == 200:  # 201 Created
    print("Request was successful!")
    response_data = response.json()
    print("Response JSON Data:", response_data)

    # Checking the structure of the response_data
    print("Response Data Keys:", response_data.keys())

    # Try to access the session token
    if 'data' in response_data:
        session_token = response_data['data'].get('session_token')
        print("Session Token:", session_token)
    else:
        print("Key 'data' not found in the response data.")
else:
    print(f"Failed with status code: {response.status_code}")



