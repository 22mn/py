from initdata import db
import pickle

for key, record in db.items():
	recfile = open(key +".pkl", "wb")
	pickle.dump(record,recfile)
	recfile.close()
