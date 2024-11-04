import pickle
pickle_off=open("amit.txt","rb")
data = pickle.load(pickle_off)
print(data)