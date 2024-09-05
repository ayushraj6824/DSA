precedence ={
    '+':1,
    '-':1,
    '*':2,
    '/':2,
    '^':3

    
}


def infix_to_postfix(expression):
    stack = []  
    postfix = []
    
    for char in expression:
        
        if char.isalnum():
            postfix.append(char)
        
        elif char == '(':
            stack.append(char)
        
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

        else:
            
            while stack and stack[-1] != '(' and precedence[char] <= precedence[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)






expression = "A+B*C+D"
result=infix_to_postfix(expression)
print(f"Infix: {expression}")
print(f"postfix: {result}")