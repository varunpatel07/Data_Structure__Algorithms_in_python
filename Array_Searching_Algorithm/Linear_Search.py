import sys
"""In this Algorithm we sequentially move to every element and compare it with a desired element if the element is found we return 
index of that elemeent. if the element is noot found we return -1(Invalid value)

Complexcity= O(n)

"""
def LinearSearch(arr,val1):
    for i in range(len(arr)):
        if(val1==arr[i]):
            return i
    #raise Exception("Value Not Found") or
    return -sys.maxsize





arr=[2,3,5,62,9,1,4,2,7,9,3,22]
print(LinearSearch(arr,0))

