import pickle
suefile = open("sue.pkl", "rb")
sue = pickle.load(suefile)
suefile.close()
sue["pay"] = 55000
suefile = open("sue.pkl","wb")
pickle.dump(sue,suefile)
suefile.close()