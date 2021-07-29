arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
cu=0
for i in range(len(arr)-2):
    for j in range(i+1,len(arr)-1):
        if(abs(arr[i]-arr[j])<=a):
            for k in range(j+1,len(arr)):
                #print("yes")
                if (abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c):
                    print("count")
                    c+=1
print(c)
        
"""        triplet = 0
        length = len(arr)
        for i in range(length - 2):
            for j in range(i + 1, length - 1):
                if abs(arr[i] - arr[j]) <= a:
                    for k in range(j + 1, len(arr)):
                        if (abs(arr[j] - arr[k]) <= b and
                            abs(arr[i] - arr[k]) <= c):
                            triplet += 1 
        return triplet""" 
n=[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]
n[0][:2]=[None,None]
print(n[0])