from numpy import *

arr=array([10,200,30,90])
maxval=arr[0]
print(len(arr))
print()

for i in range(len(arr)):
    if maxval < arr[i]:
        maxval = arr[i]
print(maxval)
print("=============================")
print(max(arr))