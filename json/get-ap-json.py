from urllib.request import Request, urlopen
import json
req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')
response = urlopen(req)
response_string = response.read().decode('utf-8')
# print(response_string)
json_obj = json.loads(response_string)
# print(json.dumps(json_obj, sort_keys=True, indent=4))

access_points = json_obj['accessPoints']
for ap in access_points:
    print(f"Access Point: {ap['name']} \t MAC: {ap['radioMacAddress']} \t IP: {ap['ipAddress']} \t Mode: {ap['apMode']}")

response.close()
