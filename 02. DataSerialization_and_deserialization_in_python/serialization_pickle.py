import pickle

friends = {'Dan': [20, 'London', 3234543], 'Maria': [25, 'Madrid', 43562543]}

# with open('friends.txt', 'w') as f:
#     # below will produce an error: "write() argument must be str, not dict"
#     f.write(friends)

# pickel works with binary files not text files
with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)