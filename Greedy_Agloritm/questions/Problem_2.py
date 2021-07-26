import sys
"""
This is a problem from Coursera

You have a car such that if you fill it up to full tank, you can travel with it up to 400 kilometers without refilling it.
And you need to get from point A to point B, and the distance between them is 950 kilometers. Of course, you need to refill
on your way, and luckily, there are a few gas stations on your way from A to B. 
"""

def FillFuel(pump,curr_fuel,curr_distance,max_dist,i=0):
    if(curr_fuel<0 or i>=len(arr)): # Fail condition
        print("Not Possible")
        return sys.maxsize
    if(curr_distance+curr_fuel>=max_dist): # succuess condition
        return 0
    x=FillFuel(pump,400,arr[i],max_dist,i+1)+1      #fill at fuel station
    y=FillFuel(pump,curr_fuel-curr_distance,arr[i],max_dist,i+1)   #do not fill at fuel station

    return min(x,y) #return the choice which gives minimum answer
    


def FillFuelGreedy(arr,max_fuel,max_dist):
    
    refill,curr_val=0,0
    while(arr[curr_val]<max_dist): # doing the step untill we reach the destination
        lastfill=curr_val
        while(curr_val<len(arr)-1 and arr[curr_val]<max_dist and arr[curr_val+1]-arr[lastfill]<=max_fuel): # choosing the farthest point which we can reach
            curr_val+=1
        if(curr_val==lastfill):
            print("NOT POSSIBLE")
            return
        if(arr[curr_val]<max_dist):
            refill+=1
            #+print("refill")
    print(refill)
    

arr=[200,375,550,750,950]
n_arr=[0,200,375,550,750,950,1000]
FillFuelGreedy(n_arr,400,1000)
max_fuel=400
final_dest=1000

#print(FillFuel(arr,400,0,300))
