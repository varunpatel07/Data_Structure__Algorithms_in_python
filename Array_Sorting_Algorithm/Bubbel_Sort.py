"""
It is the most basic type of sorting algorithm in which we compare each element with its adjecent element and swap them
in each iteration we get a greatest value and the end.

Iterative Algorithm
Inplace Algorithm-->(we directly change inside main arr)
Time Complexity-->O(n^2)

"""


def Binary_Sort(arr):
    for i in range(len(arr)-1):
        swapped=False
        for j in range(len(arr)-1-i):
            if(arr[j]>arr[j+1]):  # change sign to sort in decending order
                swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if(not(swapped)):
            print("Sorting Complete")
            break
    print(arr)
    return arr


a=[1,2,3,4,5]
Binary_Sort(a)