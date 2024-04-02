def evaluate_postfix(exp):
    stack = []
    
    for char in exp:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 // operand2)

    return stack.pop()
    
exp = input().strip()

print(evaluate_postfix(exp))
                
