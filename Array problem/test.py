import sys
cap_val=list(map(int,input().split()))
leak_val=list(map(int,input().split()))
dummy=[] #result
maxleak=sys.maxsize #
for i in range(len(cap_val)): #lop
    leak=cap_val[i]//leak_val[i] 
    maxleak=min(leak,maxleak)
    dummy.append(leak)

for idx,item in enumerate(dummy):
    if(item==maxleak):
        print(idx,end=",")
