"""
Given an array with all distinct elements, find the largest three elements. Expected time complexity is O(n) and extra space is O(1). 
Examples :

Input: arr[] = {10, 4, 3, 50, 23, 90}
Output: 90, 50, 23
"""

def sol(arr):
    f,s,t=0,0,0
    for item in arr:
        if(item>f):
            t=s
            s=f
            f=item
        elif(item>s):
            t=s
            s=item
        elif(item>t):
            t=item
    return [f,s,t]
arr=[10, 4, 3, 50, 23, 90]
print(sol(arr))