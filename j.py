import requests,json
"""

data = {"president":
			{"name":"Zaphod Beeblebrox",
			 "species":"Betelgeusian"}}
#write
with open("data_file.json","w") as write_file:
	json.dump(data,write_file)
json_string = json.dumps(data)

#read
with open("data_file.json","r") as read_file:
	data = json.load(read_file)
data["president"]
"""
response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)