"""
Given an array arr[] of size n, find the first repeating element. The element should occurs more than once and the
index of its first occurrence should be the smallest.

Example 1:

Input:
n = 7
arr[] = {1, 5, 3, 4, 3, 5, 6}
Output: 2
Explanation: 
5 is appearing twice and 
its first appearence is at index 2 
which is less than 3 whose first 
occuring index is 3.
"""
def sol1(arr):
    freq=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]==arr[j]):
                freq+=1
        if(freq>1):
            return freq
    return -1

def sol2(arr):
    a={}
    for item in arr:
        if(item not in a):
            a[item]=0
        a[item]+=1
            
    for item,val in a.items():
        if(val>1):
            print(item)
            return val
    return -1
arr=[1, 5, 3, 4, 3, 5, 6]
print(sol1(arr))
print(sol2(arr))
