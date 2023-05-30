import pickle

filename = 'E:\cse 498r\svm.pkl'
with open(filename, 'rb') as file:
    loaded_model = pickle.load(file)

print(loaded_model)