import shelve
from person_alternative import Person, Manager

bob = Person("Bob Smith", 22, 40000, "software")
sue = Person("Sue Jones", 21, 35000, "hardware")
tom = Manager("Tom Hook", 36, 50000)

db = shelve.open("class-shelve")
db["bob"] = bob
db["sue"] = sue
db["tom"] = tom
db.close()