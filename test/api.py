import requests

# Endpoint and headers
endpoint = "https://nerv.cards/api/v1/contacts/mQaSqrjsMADzXAEzhoFM"
headers = {"Authorization": "Bearer NkF1FDvOTEpQzqXHMNeKVOfvSsBYa3Q9"}

# Call endpoint with Authorization
response = requests.delete(endpoint, headers=headers)

print(response.status_code)
