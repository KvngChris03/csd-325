"""
CSD-325 - Module 9: Custom API Program
Christopher (CJ) Craig

API used: Advice Slip API (https://api.adviceslip.com)
No API key is required. The API returns a random piece of advice as JSON.
"""

import requests

url = "https://api.adviceslip.com/advice"

# --- Test the connection ---
response = requests.get(url)
print("Connection test status code:", response.status_code)

# --- Print the raw, unformatted response ---
print("\nRaw response (no formatting):")
print(response.text)

# --- Print the response formatted the same way as the tutorial program ---
data = response.json()
slip = data["slip"]

print("\nFormatted response:")
print("--------------------")
print(f"Advice Slip #{slip['id']}")
print(f"\"{slip['advice']}\"")
