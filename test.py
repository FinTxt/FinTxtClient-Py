import json
import requests

# Token 
token = "0856c8e0-9157-4a1b-9bbe-72112f0b6c1f"
url = "http://127.0.01:8000/portfolio/historic"

# Request 
req = {
    "identifiers":["TRI.TO", "IBM.N", "RRD.N", "SPGI.N", "INTU.OQ", "RELN.AS", "WLSNc.AS", "REL.L"],
    "weights":[0.3, 0.1,0.05,0.05, 0.2,0.1,0.1,0.1],
    "date":"09-07-2018",
    "type":"companies",
    "language":"english"
}

# Headers 
headers = {"API-TOKEN":token}

# To json 
req_json = json.dumps(req)

# Send request 
r = requests.post(url, data = req_json, headers=headers)

# Print content
print(r.content)

# Try get 
r = requests.get("http://127.0.01:8000/live/companies/english?q=TRI.TO",
                 headers=headers)
c = json.loads(r.content)

