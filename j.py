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

todos_by_user = {}

for todo in todos:
	if todo["completed"]:
		try:
			todos_by_user[todo["userId"]] += 1
		except KeyError:
			todos_by_user[todo["userId"]] = 1
top_users = sorted(todos_by_user.items(),key=lambda x: x[1],reverse=True)

max_complete = top_users[0][1]

users = []

for user,num_complete in top_users:
	if num_complete < max_complete:
		break
	users.append(str(user))

max_users = " and ".join(users)
