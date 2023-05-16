import pickle

# Open the file for reading in binary mode
with open("C:\\python\\diplomski_em\\ratings\\2020-01_demo.pickle", 'rb') as f:
    obj = pickle.load(f)

with open("C:\\python\\diplomski_em\\ratings\\2020-01-01.pickle", 'rb') as f:
    obj2 = pickle.load(f)

# Print the object

for i in range(10):
    print(obj[1][i])
    print(obj2[1][i])
