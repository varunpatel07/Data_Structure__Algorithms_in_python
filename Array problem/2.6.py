"""
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
"""

n1 = 6
A = [1, 5, 10, 20, 40, 80]
n2 = 5
B = [6, 7, 20, 80, 100]
n3 = 8
C = [3, 4, 15, 20, 30, 70, 80, 120]

i=j=k=0

a=set(A)
b=set(B)
c=set(C)
freq={}
for item in a:
    if(item not in freq):
        freq[item]=0
    freq[item]+=1
for item in b:
    if(item not in freq):
        freq[item]=0
    freq[item]+=1
for item in c:
    if(item not in freq):
        freq[item]=0
    freq[item]+=1

for item,val in freq.items():
    if(val==3):
        print(item)




