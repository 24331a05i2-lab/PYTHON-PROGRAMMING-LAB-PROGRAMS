tuples = [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
sortedList = sorted(tuples, key=lambda x: x[1])
print("Sorted list:", sortedList)