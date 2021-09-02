"""
Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

Example 1:

Input:
5
4 2 -3 1 6
"""

#O(n^2)
def sol1(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(sum(arr[i:j])==0):
                return "yes"
    return "no"

def sol2(arr):
    dummy=[]
    sumv=0
    for item in arr:
        sumv+=item
        if(sumv==0 or sumv in dummy):
            return "YES"
        else:
            dummy.append(sumv)
    return "NO"

arr=[4,2,-4,1,6]
print(sol1(arr))
print(sol2(arr))