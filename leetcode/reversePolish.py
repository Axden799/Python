def evalRPN(tokens):
    x = 0
    
    while len(tokens) > 1:
        while tokens[x] not in "+-*/":
            x += 1
            
        num1 = int(tokens[x-2])
        num2 = int(tokens[x-1])
        op = tokens[x]
        res = 0

        if op == "+": tokens[x] = num1 + num2
        elif op == "-": tokens[x] = num1 - num2
        elif op == "*": tokens[x] = num1 * num2
        elif op == "/": tokens[x] = int(num1 / num2)
            
        tokens.pop(x-2)
        tokens.pop(x-2)
        x -= 1

    return tokens[0]

def stackEvalRPN(tokens):
    stack = []
        
    for x in range(len(tokens)):
        if tokens[x] not in "+-*/":
            stack.append(int(tokens[x]))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            operation = tokens[x]

            if operation == "+": stack.append(num1 + num2)
            if operation == "-": stack.append(num1 - num2)
            if operation == "*": stack.append(num1 * num2)
            if operation == "/": stack.append(int(num1 / num2))
        
    return stack.pop()