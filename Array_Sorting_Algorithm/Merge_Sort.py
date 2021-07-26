"""
Merge sort is one of the most efficient sorting algorithms. It works on the principle of Divide and Conquer. 
Merge sort repeatedly breaks down a list into several sublists until each sublist consists of a single element
and merging those sublists in a manner that results into a sorted list.

Recurssive
Complexity= nLogn

"""

def MergeSort(arr):
    if(len(arr)>1):
        mid=len(arr)//2
        left=MergeSort(arr[:mid])
        right=MergeSort(arr[mid:])


        i=j=k=0
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]): #change sign to reverse the order
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1

        while(i<len(left)):
            arr[k]=left[i]
            i+=1
            k+=1

        while(j<len(right)):
            arr[k]=right[j]
            j+=1
            k+=1

    return arr

arr=[2,3,1,5,4]
print(MergeSort(arr))

