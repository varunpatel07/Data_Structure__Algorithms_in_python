"""
Given an array of positive integers, sort the array in decreasing order of count of set bits in binary representations of array elements. 
For integers having the same number of set bits in their binary representation, sort according to their position in the original array
i.e., a stable sort. For example, if the input array is {3, 5}, then the output array should also be {3, 5}. Note that both 3 and 5 have
the same number set bits.

Input: arr[] = {5, 2, 3, 9, 4, 6, 7, 15, 32};
Output: 15 7 5 3 9 6 2 4 32
Explanation:
The integers in their binary representation are:
    15 -1111
    7  -0111
    5  -0101
    3  -0011
    9  -1001
    6  -0110
    2  -0010
    4- -0100
    32 -10000
hence the non-increasing sorted order is:
{15}, {7}, {5, 3, 9, 6}, {2, 4, 32}

"""
#SOLUTION-1
def dectobin(n):
    if(n==0 or n==1):
        return n
    else:
        return dectobin(n//2)*10+(n%2)

arr=[5,2,3,9,4,6,7,15,32]
dummy=[]
for item in arr:
    
    dummy.append((item,str(dectobin(item)).count("1")))
out=sorted(dummy,key=lambda x:x[1],reverse=True)
print(list(zip(*out))[0])

aux=[]
def bincount(n):
    c=0
    while(n!=0):
        if(n&1==1):
            c+=1
        n=n>>1
    return c 

#SOLUTION 2
def insertionsort():
    for i in range(len(arr)):
        key1=aux[i]
        key2=arr[i]
        j=i-1
        while(j>=0 and aux[j]<key1):
            aux[j+1]=aux[j]
            arr[j+1]=arr[j]
            j-=1
        aux[j+1]=key1
        arr[j+1]=key2

for item in arr:

    aux.append(bincount(item))
insertionsort()
print(arr)

