"""
Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


Example 1:

Input:
N = 4, K = 6
arr[] = {1, 5, 7, 1}
Output: 2
Explanation: 
arr[0] + arr[1] = 1 + 5 = 6 
and arr[1] + arr[3] = 5 + 1 = 6.
"""
import collections

def sol(arr,n,k):
    s=collections.defaultdict(int)
    c=0
    for item in arr:
        if(k-item in s):
            print("found")
            c+=s[k-item]
        s[item]+=1
        print(s)

    print(c)
sol([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1],4,11)