"""
Given an unsorted array arr[] of size N having both negative and positive integers. The task is place all negative element at the end of array without changing the order of positive element and negative element.

 

Example 1:

Input : 
N = 8
arr[] = {1, -1, 3, 2, -7, -5, 11, 6 }
Output : 
1  3  2  11  6  -1  -7  -5

"""
def solution(arr):
    narr=[0]*len(arr)
    j=0
    for i in arr:
        if(i>0):
            narr[j]=i
            j+=1
    for i in arr:
        if(i<0):
            narr[j]=i
            j+=1
    print(narr)
solution([1, -1, 3, 2, -7, -5, 11, 6])
