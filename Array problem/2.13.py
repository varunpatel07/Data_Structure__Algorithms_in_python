import sys
arr=[3,4,1,9,56,7,9,2]
n=5


arr.sort()
i=0
j=n-1
minv=sys.maxsize
while(j<len(arr)):
    minv=min(minv,arr[j]-arr[i])
    i+=1
    j+=1
print(minv)
