#time:O(n)
#space:O(N)
arr=[
    [1,1,1,1,1], #11111
    [1,0,1,0,1], #10101
    [1,0,1,0,1], #10101
    [1,0,1,0,1], #10101
    [1,1,0,1,1] #11011
]
dum={}
for idx,item in enumerate(arr):
    temp="".join(list(map(str,item)))
    if(temp not in dum):
        dum[temp]=[0,idx]
    dum[temp]=[dum[temp][0]+1,idx]

for key,val in dum.items():
    if(val[0]==1):
        print(val[1])