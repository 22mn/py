import shelve
db = shelve.open("class-shelve")

sue = db["sue"]
sue.giveRaise(0.1)
db["sue"]=sue

db.close()