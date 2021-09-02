"""
Kadane's Algorithm 
Medium Accuracy: 51.0% Submissions: 100k+ Points: 4
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


Example 1:

Input:
N = 5
arr[] = {1,2,3,-2,5}
Output:
9
Explanation:
Max subarray sum is 9
of elements (1, 2, 3, -2, 5) which 
is a contiguous subarray.
"""


def sol(arr):
    curr=0
    maxs=0
    for item in arr:
        curr=max(item+curr,item)
        maxs=max(maxs,curr)
    return maxs

print(sol([1,2,3,-2,5]))