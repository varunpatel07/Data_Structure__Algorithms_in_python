import sys

"""
In this algorithm we take a SORTED array and find the mid element, then we check if our desired element is smaller or bigger than the
mid element. if a element is smaller than the mid element then we perform the same operation on elements on left hand side of mid element 
and vice versa

Complexity--> O(log N)

"""

def BinarySearchRecursive(arr,val,low,high):
    if(high<low):
        return -sys.maxsize
        
    mid=low+(high-low)//2
    if(arr[mid]==val):
        return mid
    if(arr[mid]>val):
        return BinarySearchRecursive(arr,val,low,mid-1)
    else:
        return BinarySearchRecursive(arr,val,mid+1,high)

def BinarySearchIterative(arr,val):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=low+(high-low)//2
        if(arr[mid]==val):
            return mid
        if(arr[mid]>val):
            high=mid-1
        else:
            low=mid+1

    return -sys.maxsize

arr=[1,2,3,4,5,6,7,8,8,22,44,55]
print(BinarySearchRecursive(arr,55,0,len(arr)-1))
print(BinarySearchIterative(arr,1))