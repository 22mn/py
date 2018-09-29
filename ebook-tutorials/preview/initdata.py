
# initialize data to be stored in files, pickles, shelves

# records
bob = {"name": "Bob Smith", "age": 22, "pay": 50000, "job": "dev"}
sue = {"name": "Sue Jones", "age": 21, "pay": 45000, "job": "alc"}
tom = {"name": "Tom", "age": 50, "pay": 60000, "job": "mgr"}


# database
db = {}
db["bob"] = bob
db["sue"] = sue
db["tom"] = tom

if __name__ == '__main__':
	for key in db:
		print(key, "=>\n ", db[key])