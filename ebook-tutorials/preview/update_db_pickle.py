import pickle
dbfile = open("people-pickle","rb")
db = pickle.load(dbfile)
dbfile.close()

db["sue"]["pay"] = 55000
db["tom"]["name"] = "Tom Hook"

dbfile = open("people-pickle","wb")
pickle.dump(db,dbfile)
dbfile.close()