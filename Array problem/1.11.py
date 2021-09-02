#find the length of longest substring with all unique charcters
#here ans is placem becuase no charcter is repeated he4re
inp1="place mentpreparation"

dum={}
start=0
maxl=0
for end in range(len(inp1)):
    if(inp1[end] in dum):
            start=max(start,dum[inp1[end]]+1)
    maxl=max(maxl,end-start+1)
    dum[inp1[end]]=end
print(maxl)