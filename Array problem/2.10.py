"""
Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.

Examples : 

Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}

Input:  arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
output: arr[] = {-5, 5, -2, 2, -8, 4, 7, 1, 8, 0}
"""



def sol(arr):
    neg=[]
    pos=[]
    for item in arr:
        if(item<0):
            neg.append(item)
        else:
            pos.append(item)
    i=j=c=0
    flag=False
    while(i<len(pos) and j<len(neg)):
        if(flag):
            arr[c]=pos[i]
            i+=1
            flag=False
        else:
            arr[c]=neg[j]
            j+=1
            flag=True
        c+=1
    while(i<len(pos)):
        arr[c]=pos[i]
        i+=1
        c+=1
    while(j<len(neg)):
        arr[c]=neg[j]
        j+=1
        c+=1
    print(arr)

def sol2(arr):
    arr.sort()

    i=j=0
    while(arr[j]<0 and j<len(arr)):
        j+=1
    print(arr)
    print(j)

# Below is the implementation of the above approach

def rearrange(arr, n):
	# sort the array
	arr.sort()

	# initialize two pointers
	# one pointing to the negative number
	# one pointing to the positive number
	i, j = 1, 1
	while j < n:
		if arr[j] > 0:
			break
		j += 1

	# swap the numbers until the given condition gets satisfied
	while (arr[i] < 0) and (j < n):
		# swaping
		arr[i], arr[j] = arr[j], arr[i]
		
		# increment i by 2
		# because a negative number is followed by a positive number
		i += 2	
		j += 1
	
	return(arr)



# Driver Code
# Given array
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

ans = rearrange(arr, len(arr))
for num in ans:
	print(num, end = " ")

# This code is contributed by Tharun Reddy

arr=[-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
sol(arr)
sol2(arr)