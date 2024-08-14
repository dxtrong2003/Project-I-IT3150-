import ast

operatorx = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}

def safe_eval(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right
    elif isinstance(node, ast.UnaryOp):
        operand = safe_eval(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        elif isinstance(node.op, ast.USub):
            return -operand
    else:
        raise ValueError(f"Unsupported type: {node}")

def valid(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                return False
        return True
    except (SyntaxError, ValueError):
        return False

def i_to_post(infix):
    if not valid(infix):
        return "Invalid expression"
    stack = []
    op = []
    for char in infix:
        if char.isalnum():
            op.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while len(stack) > 0 and stack[-1] != '(':
                op.append(stack.pop())
            stack.pop()
        else:
            while len(stack) > 0 and stack[-1] != '(' and operatorx[char] <= operatorx[stack[-1]]:
                op.append(stack.pop())
            stack.append(char)

    while len(stack) > 0:
        op.append(stack.pop())

    return ' '.join(op)


#print(i_to_post("a + b * ( c ^ d - e ) ^ ( f + g * h ) - i"))


def i_to_pre(infix):
    if not valid(infix):
        return "Invalid expression"
    a = list(infix[::-1])
    for i in range(len(a)):
        if a[i] == '(':
            a[i] = ')'
        elif a[i] == ')':
            a[i] = '('
    return i_to_post(''.join(a))[::-1]
