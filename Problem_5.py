"""
Parenthesis matching

In both of these examples, parentheses must appear in a balanced fashion. 
Balanced parentheses means that each opening symbol has a corresponding closing symbol 
and the pairs of parentheses are properly nested.

(()()()())--> balanced
()))--> unbalanced
"""

#working
def parenthesis(val):
    stack=[]
    for bracket in val:
        if(bracket=="("):
            stack.append("(")
        else:
            if(len(stack)==0):
                return "unbalanced"
            if(stack[-1]=="("):
                stack.pop()
            else:
                return "Unbalanced"
    if(len(stack)==0):
        return "Balanced"
    else:
        return "Unbalanced"

print(parenthesis("(((())"))