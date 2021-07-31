class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self,data):
        self.length=1
        self.head=self.tail=Node(data)

    def add(self,data):
        if(self.tail!=None):
            node=Node(data)
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            

    

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

print()
obj.display()
obj.search(2)
print(obj.isempty())
obj.size()