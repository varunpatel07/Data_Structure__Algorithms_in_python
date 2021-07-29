class Node:
    def __init__(self,data):
        self.data=data
        
        self.next=None
class LinkedList:
    def __init__(self,data):
        self.length=1
        self.head=Node(data)

    def add(self,data):
        self.length+=1
        if(self.head!=None):
            curr=self.head
            while(curr.next!=None):
                curr=curr.next
            curr.next=Node(data)
        else:
            self.head=Node(data)

    def remove(self,data):
        curr=self.head
        prev=None
        if(curr.data==data):
            print(f"{curr.data} removed")
            self.head=self.head.next
        else:
            while(curr!=None):
                if(curr.data!=data):
                    prev=curr
                    curr=curr.next
                else:
                    break
                    
            if(curr!=None):
                print(f"{curr.data} removed")
                prev.next=curr.next
            else:
                print("NO VALUE FOUND")
        self.length-=1

    def search(self,data):
        curr=self.head
        while(curr!=None):
            if(curr.data==data):
                print(f"\nYes element {data} exist")
                return
            curr=curr.next
        print(f"\n{data} not present")

    def isempty(self):
        return self.length==0
    def size(self):
        print(f"length of linked list is {self.length}")
        return self.length

    def display(self):
        curr=self.head
        while(curr!=None):
            print(f"{curr.data}--->",end="")
            curr=curr.next



        
obj=LinkedList(1)
obj.add(2)
obj.add(3)
obj.display()
print()
obj.remove(1)
print()
obj.display()
obj.search(5)
print(obj.isempty())
obj.size()