from initdata import *
import shelve
db = shelve.open("people-shelve")
sue = db["sue"]
sue["pay"] = 55000
db["sue"] = sue
db["tom"] = tom
db.close()