"""
Given an array, rotate the array by one position in clock-wise direction.

Example 1:

Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4
"""
def sol(arr):
    key=arr[-1]
    j=len(arr)-2
    while(j>=0):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
    print(arr)
sol([1,2,3,4,5])