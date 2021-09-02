"""
Given an array of size N-1 such that it only contains distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
"""

def sol(arr,n):
    total=0
    for item in arr:
        total+=item
    return ((n*(n+1))//2)-total
print(sol([1,2,3,5],5))