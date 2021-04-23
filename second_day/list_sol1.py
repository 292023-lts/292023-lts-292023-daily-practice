from array import *
arr = array('i', [])
n = int(input("enter number of elements:"))
for i in range(n):
    arr.append(int(input("enter the array elements:")))
print("entered array is:")
for i in range(len(arr)):
    print(arr[i])
largest = max(arr)
print("Largest element:",largest)
smallest = min(arr)
print("Smallest number:", smallest)
arr.remove(smallest)
secsmall = min(arr)
print("Second Smallest number:",secsmall)