import requests
import json


#API_URL
API_URL = "https://reqres.in/api/users?page="

#Total number of pages
NUM_OF_PAGES = 12

totalUsers = 0
for i in range(NUM_OF_PAGES):
	apiResp = requests.get(API_URL+ str(i+1))
	if apiResp.status_code == 200:
		jsonData = apiResp.json()
		totalData = len(jsonData.get('data'))
		if totalData > 0:
			totalUsers = totalUsers + totalData
	else:
		resp = {
		    "status": 404,
		    "msg": "API not called successfully "
		}
		print(json.dumps(resp))
resp = {
    "status": 200,
    "msg": "success",
    "totalUsers": str(totalUsers)
}
print(json.dumps(resp))