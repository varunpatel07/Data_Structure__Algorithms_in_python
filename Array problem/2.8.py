"""

Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.

Example 1:

Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is 
the only number occuring once.
Hence, the output is 3. 
"""

def sol(arr):
    a={}
    for item in arr:
        if(item not in a):
            a[item]=0
        a[item]+=1
    
    for item,val in a.items():
        if(val==1):
            return item
    return -1
arr=[-1, 2, -1, 3, 2]

print(sol(arr))