"""
QUICKSORT
"""

def partition(arr,low,high):
    pivot=arr[low]
    pivoti=low
    start=low+1
    end=high
    while(start<end):
        while(arr[start]<=pivot and start<=high):
            start+=1
        while(arr[end]>pivot and end>=0):
            end-=1

        if(start<end):
            arr[start],arr[end]=arr[end],arr[start]
    arr[pivoti],arr[end]=arr[end],arr[pivoti]
    return end



def quicksort(arr,low,high):
    if(low<high):
        p=partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

arr=[2,1,3,5,4]
quicksort(arr,0,4)
print(arr)