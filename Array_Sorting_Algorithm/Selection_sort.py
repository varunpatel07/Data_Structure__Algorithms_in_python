"""
It is modified version of Bubble sort where we find tha minimum element and then replace it with the first, second ..... positions

Stable Sort
Inplace Sort
Time Complexity--> O(n^2)

"""

def SelectionSort(arr):

    for index in range(len(arr)):
        min_idx=index
        for i in range(index,len(arr)):
            if(arr[i]<arr[min_idx]): #reverse the sign for decending order
                min_idx=i
        arr[index],arr[min_idx]=arr[min_idx],arr[index]
    print(arr)



arr=[2,3,1,5,4]
SelectionSort(arr)