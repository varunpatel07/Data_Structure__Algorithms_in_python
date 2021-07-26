"""
Leetcode search insert position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where
it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
"""


def searchInsert(nums,val):
    low=0
    high=len(nums)-1

    while(low<=high):
        
        mid=low+(high-low)//2

        if(nums[mid]==val):
            #print("found")
            return mid
        if(val<nums[mid]):
            high=mid-1
        else:

            low=mid+1
    
    if(arr[mid]>val):
        return mid
    else:
        return mid+1
    #pass

arr=[1,3,5,6]
print(searchInsert(arr,4))

