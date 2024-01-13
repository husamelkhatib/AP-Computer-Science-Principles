import time
from SearchAlgorithms import linear_search, binary_search
def print_search(type, result, time):
if result != -1:
    print(type + "Number found at index" + result)
else:
    print(type + "Number not found")
print("Search time: " + time + "seconds")
