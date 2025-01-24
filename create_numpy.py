import numpy as np
x = np.array([1,2,3,4])
print(x)

print(type(x))


l = list(map(int, input("Enter the integers with white space: ").split()))
print(np.array(l))


m = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    k = input("Enter the element : ")
    m.append(int(k))

print(np.array(m))
