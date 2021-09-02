"""
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in union.

Example 1:

Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
"""
def sol1(arr1,arr2):
    res=set()
    for item in arr1:
        res.add(item)
    for item in arr2:
        res.add(item)
    return len(res)
def sol2(arr1,arr2):
    return len(set(arr1).union(set(arr2)))
print(sol1([1,2,3,4,5],[1,2,3]))
print(sol2([1,2,3,4,5],[1,2,3]))

