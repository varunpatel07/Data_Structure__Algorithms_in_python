import sys
"""
Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways. 

Always pick first element as pivot.
Always pick last element as pivot 
"""
def Partition(arr,low,high):
    pivot_index=low
    pivot_val=arr[pivot_index]
    while(low<high):
        while(low<len(arr) and arr[low]<=pivot_val):
            low+=1
        while(arr[high]>pivot_val):
            high-=1
        if(low<high):
            arr[low],arr[high]=arr[high],arr[low]
    arr[high],arr[pivot_index]=arr[pivot_index],arr[high]
    return high
    

def QuickSort(arr,low,high):
    if(low<high):


        p=Partition(arr,low,high)

        QuickSort(arr,low,p-1)
        QuickSort(arr,p+1,high)
    
arr=[2,1,5,4,3]
#Partition(arr,0,len(arr)-1)
QuickSort(arr,0,len(arr)-1)
print(arr)