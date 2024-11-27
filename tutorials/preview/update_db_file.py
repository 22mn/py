from make_db_file import loadDbase, storeDbase

db = loadDbase()
db["sue"]["pay"] = 50000
db["tom"]["name"] = "Tom Hook"
storeDbase(db)