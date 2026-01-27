list= [10, 20, 30, 40]
print("Original List:", list)
print("Length of list:", len(list))
list.append(50)
print("After append(50):", list)
list.insert(2, 25)
print("After insert(2, 25):", list)
list2 = [60, 70]
list.extend(list2)
print("After extend([60, 70]):", list)
list.remove(30)
print("After remove(30):", list)
list.sort()
print("After sort():", list)