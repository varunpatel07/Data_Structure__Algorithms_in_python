"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at 
the correct position in the sorted part.


Sorting In Place: Yes
Stable: Yes
Online: Yes

Time Complexity: O(n^2) 
Auxiliary Space: O(1)
"""
def InsertionSort(arr):

    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while(j>=0 and key<arr[j]):  #change sign to reverese the order
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    print(arr)

arr=[2,3,1,5,4]
InsertionSort(arr)