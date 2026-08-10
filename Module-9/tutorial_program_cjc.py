"""
CSD-325 - Module 9: API Tutorial Program
Christopher (CJ) Craig

Tutorial: Working with the Open Notify API.
Step 1 tests the connection to the API.
Step 2 retrieves and formats the list of astronauts currently in space.
"""

import requests

# --- Test the API connection ---
response = requests.get("http://api.open-notify.org")
print("Connection test status code:", response.status_code)

# --- Retrieve current astronauts in space ---
astros_response = requests.get("http://api.open-notify.org/astros.json")
data = astros_response.json()

print("\nCurrent People in Space")
print("------------------------")
print(f"There are currently {data['number']} people in space.\n")

for person in data["people"]:
    print(f"{person['name']:<25} aboard the {person['craft']}")
