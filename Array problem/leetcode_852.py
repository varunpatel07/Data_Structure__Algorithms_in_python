"""
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1"""

def sol1_n(self, arr: List[int]) -> int:
    maxe=0
    midx=0
    for idx,item in enumerate(arr):
        if(item>maxe):
            maxe=item
            midx=idx
    return midx


def sol2_logn(self, arr: List[int]) -> int:
    start=0
    end=len(arr)-1
    while(start<end):
        mid=start+(end-start)//2
        if(arr[mid]>arr[mid+1]):
            end=mid
        else:
            start=mid+1
    return start