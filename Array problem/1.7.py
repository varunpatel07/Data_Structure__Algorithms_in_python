"""
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


Example 1:

Input: 
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated 
into ascending order.
"""
def solution(arr):
    count_arr=[0,0,0]
    for item in arr:
        count_arr[item]+=1
    arr=[0]*count_arr[0]
    arr.extend([1]*count_arr[1])
    arr.extend([2]*count_arr[2])
    return arr

print(solution([0,2,2,0]))