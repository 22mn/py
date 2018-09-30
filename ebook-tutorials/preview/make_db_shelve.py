from initdata import *
import shelve
db = shelve.open("people-shelve")
db["bob"] = bob
db["sue"] = sue
db.close()
