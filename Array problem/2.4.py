"""
Find duplicates in an array 
Easy Accuracy: 20.69% Submissions: 100k+ Points: 2
Given an array a[] of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array.

Example 1:

Input:
N = 4
a[] = {0,3,1,2}
Output: -1
Explanation: N=4 and all elements from 0
to (N-1 = 3) are present in the given
array. Therefore output is -1.
"""
def sol(arr,n):
    freq=[0]*n
    for item in arr:
        freq[item]+=1
    hasduplicate=False
    for i in range(n):
        if(freq[i]>1):
            print(i)
            hasduplicate=True
    if(not hasduplicate):
        print(-1)
sol([2,3,1,2,3],5)