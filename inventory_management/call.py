import requests

url = "http://127.0.0.1:8003/api/items/4/"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI3NzY4Mjc5LCJpYXQiOjE3Mjc3NjQ2NzksImp0aSI6ImNkZWQ3MjE5MmY2YTQ5OTRiOTQ5ZTJmMmY1NzQxMjQ5IiwidXNlcl9pZCI6MX0.5s2jxgfHP2U5EQruYebptNA6UAQeLRtFiUmnvdgrkZk"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
data = {
    "name": "Sample Item12",
    "asset_id":"hj11k",
    "description": "This is a sample item."
}

# response = requests.put(url, json=data, headers=headers)
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Item created successfully:", response.json())
else:
    print("Failed to create item:", response.status_code, response.text)
