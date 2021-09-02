target=[3,7,9]
arr=[3,7,11]
a1,a2={},{}
for item in target:
    if(item not in a1):
        a1[item]=0
    a1[item]+=1
for item in arr:
    if(item not in a2):
        a2[item]=0
    a2[item]+=1
print(f"{a1} {a2}")
for item,val in a2.items():
    if(item not in a1 or a1[item]!=val):
        print(False)
print(True)