"""
Given an array A of size N of integers. Your task is to find the minimum and maximum elements in the array.

 

Example 1:

Input:
N = 6
A[] = {3, 2, 1, 56, 10000, 167}
Output:
min = 1, max =  10000
"""

def Arraysort(arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
#print(Arraysort())
arr=[3,2,1,56,1000,167]
arr=Arraysort(arr)
print(f"max={arr[-1]} min={arr[0]}")
