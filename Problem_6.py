"""
Given an numsay of positive integers nums, calculate the sum of all possible odd-length subnumsays.

A subnumsay is a contiguous subsequence of the numsay.

Return the sum of all odd-length subnumsays of nums.
nums = [1,4,2,5,3]

Input: nums = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subnumsays of nums and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

"""


def solution(nums):
    ans=0
    for i in range(1,len(nums)+1,2):
        for j in range(0,len(nums)-i+1):
            print(nums[j:j+i])
            ans+=sum(nums[j:j+i])
    print(ans)
    return ans

nums = [1,4,2,5,3]
solution(nums)