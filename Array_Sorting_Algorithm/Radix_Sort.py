"""
The idea of Radix Sort is to do digit by digit sort starting from least significant digit to most significant digit. 
Radix sort uses counting sort as a subroutine to sort.


Useful when array is small and only have less postitions.....

For small array it has complexity of (nk) linear time

"""

def CountingSort(arr,pos):
    #print(arr)
    count=[0]*10
    
    for item in arr:
        ind= item//10**pos %10 
        #print(ind)
        count[ind]+=1
        
    for i in range(1,len(count)):
        count[i]+=count[i-1]

        
    print(count)
    out=[0]*len(arr)
    for item in reversed(arr):
        ind=item//10**pos %10 
        count[ind]-=1
        out[count[ind]]=item

    print(out)
    return out

def RadixSortNew(arr,maxlen):

    for i in range(maxlen):
        arr=CountingSort(arr,i)
        print("done")
    print(arr)


def RadixSort(arr,maxlen):

    for position in range(maxlen):
        aux=[[] for _ in range(10)]
        for item in arr:
            index= item//10**position % 10
            aux[index].append(item)
        arr=[array_item for item in aux for array_item in item]
    print(arr)
    






arr=[3,4,1,2,6,3,88,22,491,841]
max_len=len(str(max(arr)))
#RadixSort(arr,max_len)
RadixSortNew(arr,max_len)