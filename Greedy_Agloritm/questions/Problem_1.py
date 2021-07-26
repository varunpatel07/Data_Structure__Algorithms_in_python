"""
This problem is from Coursera

So imagine this situation. You are trying to get a job at a company and you already had a few interviews, and everything went well.
Now you have your final interview with the boss, and he tells you that he will give you an offer. But instead of negotiating your salary with you, 
he will give you a few pieces of paper with digits written on them.
And your task will be to arrange those digits in a row, so that when you read the number from left to right,
that will be your salary.


Ans--> We need to pick the highest value and put it in front basically we need to sort it in decending order
"""

def LargestSalary(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        idx=i-1
        while(idx>=0 and key>arr[idx]):
            arr[idx+1]=arr[idx]
            idx-=1
        arr[idx+1]=key
    print("".join(list(map(str,arr))))

# complexity -->O(n)

arr=[7,4,2,5,2,9,1,6]
LargestSalary(arr)