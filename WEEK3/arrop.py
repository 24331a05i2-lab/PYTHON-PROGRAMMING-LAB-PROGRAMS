import numpy as np

lst1 = [(1, 2, 3), (4, 5, 6)]

npArr = np.array(lst1)

print("NumPy 2D Array:\n", npArr)

print("Total sum of matrix:", np.sum(npArr))
print("Sum of elements in rows:", np.sum(npArr, axis=1))
print("Sum of elements in columns:", np.sum(npArr, axis=0))

print("Transpose of matrix:\n", npArr.T)

print("Maximum value in matrix:", np.max(npArr))
print("Minimum value in matrix:", np.min(npArr))

print("Flattened array:", npArr.flatten())
print("Mean of matrix elements:", np.mean(npArr))
print("Standard deviation of matrix elements:", np.std(npArr))
