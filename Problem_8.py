"""
Tree traversal using recursive and iterative code
"""

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree


class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


# A function to do inorder tree traversal
def printInorder(root):
    if(root==None):
        return
    if(root.left):
        printInorder(root.left)
    print(root.val,end=" ")
    if(root.right):
        printInorder(root.right)

def inorder(root):
    s,r=[],[]
    node=root
    while node or s:
        if(node):
            s.append(node)
            node=node.left
        else:
            node=s.pop()
            print(node.val,end=" ")
            node=node.right



# A function to do postorder tree traversal
def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val,end=" ")


# A function to do preorder tree traversal
def printPreorder(root):

	if root:

		# First print the data of node
		print(root.val,end=" ")

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)

def postorder(root):

    s,r=[],[]
    node=root
    while node or s:
        if(node):
            s.append(node)
            node=node.left
        else:
            temp=s[-1].right
            if(temp==None):
                temp=s.pop()
                print(temp.val)
                r.append(temp.val)
                while(s and s[-1].right==temp):
                    temp=s.pop
                    r.append(temp.val)

            else:
                node=temp

    return r


def preoder(root):
    s,r=[],[]
    node=root
    while s or node:
        # print(locals())
        if(node):
            print(node.val,end=" ")
            s.append(node)
            node=node.left
        else:
            node=s.pop()

            node=node.right

# Driver code
root = Node(10)
root.left = Node(None)
root.right = Node(3)
root.left.left = Node(None)
root.left.right = Node(1)
printPreorder(root)
print()
preoder(root)
print()
printInorder(root)
print()
inorder(root)
print()
printPostorder(root)
print()
print(postorder(root))