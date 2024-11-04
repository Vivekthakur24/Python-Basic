import pickle
my_list=["a","b","c","d"]
with open('amit.txt','wb') as fh:
    pickle.dump(my_list,fh)

pickle_off=open("amit.txt","rb")
data = pickle.load(pickle_off)
print(data)