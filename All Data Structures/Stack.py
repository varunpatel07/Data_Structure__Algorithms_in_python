class Stack:
    def __init__(self):
        self.__size=0
        self.__stack=[]
    
    def push(self,val):

        self.__stack.append(val)
        self.__size+=1

    def pop(self):
        self.__size-=1
        return self.__stack.pop()

    def peek(self):
        if(self.__size==0):
            return "Stack Empty"
        else:
            return self.__stack[-1]
    def size(self):
        return self.__size

