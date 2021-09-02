"""
You are given a string s. You need to reverse the string.

Example 1:

Input:
s = Geeks
Output: skeeG
Example 2:

Input:
s = for
Output: rof
"""

def reverseword(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return "".join(arr)
a="for"
print(reverseword(list(a)))