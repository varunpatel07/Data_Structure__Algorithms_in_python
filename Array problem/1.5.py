"""
Given a vector of N positive integers and an integer X. The task is to find the frequency of X in vector.

 

Example 1:

Input:
N = 5
vector = {1, 1, 1, 1, 1}
X = 1
Output: 
5
Explanation: Frequency of 1 is 5.
"""
def solution(arr,k):
    c=0
    for item in arr:
        if(item==k):
            c+=1
    return c
print(solution([1,1,1,1,1],3))