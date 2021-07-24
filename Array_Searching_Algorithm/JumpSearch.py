import sys
import math
"""
This algorithm takes a SORTED array . the idea behind this algo is that we would compare every m(siz of block, number of element to be skipped)
element. and check if it is equal to or greater then our required element if so then we would go back to previous block and do linear search
m== square root of len of array or we can take any
complexity--> O(Square root of n)

its complexity lies between binary search and linear search

"""

def JumpSearch(arr,val):
    prev_block=0
    m=int(math.sqrt(len(arr)))
    while(arr[int(min(m,len(arr))-1)]<val):
        prev_block=m
        m+=int(math.sqrt(len(arr)))
        if(prev_block>len(arr)-1):  
            return -sys.maxsize

    for idx in range(prev_block,m):
        if(val==arr[idx]):
            return idx
    return -sys.maxsize

arr=[1,2,3,4,5,6,7,8,9]
print(JumpSearch(arr,10))