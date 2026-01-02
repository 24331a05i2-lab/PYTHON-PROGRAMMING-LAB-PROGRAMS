import numpy as np

lst1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
lst2 = [2, 2, 3, 4, 5, 4, 3, 2, 6]

npLst1 = np.array(lst1)
npLst2 = np.array(lst2)

print("Sum of lists:", npLst1 + npLst2)
print("Max of npLst1:", np.max(npLst1))
print("Min of npLst1:", np.min(npLst1))
print("Mean of npLst1:", np.mean(npLst1))
print("Standard deviation:", np.std(npLst1))
print("Dimension of array:", np.ndim(npLst1))

print("Indexing from 1 to 5:", npLst1[1:5])
print("Indexing from 5 to end:", npLst1[5:])
print("Slicing from -5 to -1:", npLst1[-5:-1])
