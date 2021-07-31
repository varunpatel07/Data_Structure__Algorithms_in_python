"""
Given a collection of intervals, merge all overlapping intervals.
Input: [[1,3],[2,6],[8,10], [9,11] ,[10,12], [2,4] ,[15,18]]
Output: [[1,6],[8,12],[15,18]] 

"""
def test(i=0,arr=[],arr1=[]):
    print(f"before {i}----{locals()}")
    if(i==3):
        return
    arr.append(i)
    arr1=arr1+[i]
    test(i+1)
    print(f"after {i}----{locals()}")
test()
