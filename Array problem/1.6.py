"""
Given an array and a number k where k is smaller than the size of the array, we need to find the k’th smallest element in the given array. It is given that all array elements are distinct.

Examples:  

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15} 
k = 4 
Output: 10 
"""
def solution(arr,k):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]<key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)
    return arr[k]
print(solution([7, 10, 4, 3, 20, 15],3))
