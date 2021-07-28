"""
Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having 
distinct key values (kind of hashing). 
Then doing some arithmetic to calculate the position of each object in the output sequence.


Time Complexity-->Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input. 
Auxiliary Space: O(n+k)

1. Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K. 
2. It is not a comparison based sorting. It running time complexity is O(n) with space proportional to the range of data. 
3. It is often used as a sub-routine to another sorting algorithm like radix sort. 
4. Counting sort uses a partial hashing to count the occurrence of the data object in O(1). 
5. Counting sort can be extended to work for negative inputs also.
"""
def CountingSort(arr):
    count=[0]*len(arr)
    out=[]
    for item in arr:
        count[item]+=1
    for i in range(len(count)):
        if(count[i]!=0):
            out.extend([i]*count[i])
    print(out)

def CountingSortnew(arr):
    count=[0]*(max(arr)+1)
    for item in arr:
        count[item]+=1
    for i in range(1,len(count)):
        count[i]+=count[i-1]
    out=[0]*len(arr)
    for item in arr:
        
        count[item]=count[item]-1
        out[count[item]]=item
    print(out)




arr=[4,2,3,6,3,1,6,3,4]
CountingSort(arr)
CountingSortnew(arr)
