operators = {'+': 1, '-': 1, '*': 2, '/': 2, '**': 2, '%': 2}


def post_to_i(postfix):
    if not postfix[0].isalnum():
        return "Invalid expression"
    if len(postfix) < 3:
        return "Invalid expression"

    a = postfix.strip().split()
    i = 2
    while i < len(a):
        try:
            if operators[a[i]] == 1:
                if i == 1:
                    return "Invalid expression"
                if a[i] == "+":
                    a[i-2] = f"{a[i-2]} + {a[i-1]}"
                elif a[i] == '-':
                    if len(a[i-1]) > 1:
                        a[i-2] = f"{a[i-2]} - ({a[i-1]})"
                    else:
                        a[i-2] = f"{a[i-2]} - {a[i-1]}"
            else:
                if i == 1:
                    return "Invalid expression"
                if len(a[i-2]) > 1:
                    if len(a[i-1]) > 1:
                        a[i-2] = f"({a[i-2]}) {a[i]} ({a[i-1]})"
                    else:
                        a[i-2] = f"({a[i-2]}) {a[i]} {a[i-1]}"
                else:
                    if len(a[i-1]) > 1:
                        a[i - 2] = f"{a[i-2]} {a[i]} ({a[i-1]})"
                    else:
                        a[i - 2] = f"{a[i-2]} {a[i]} {a[i-1]}"

            del a[(i-1):(i+1)]
            i -= 2
        except KeyError:
            i += 1
            if len(a) == 3:
                break

    if len(a) < 3:
        if len(a) == 1:
            return a[0]
        return "Invalid expression"
    else:
        if a[2] not in operators:
            return "Invalid expression"
        else:
            if operators[a[2]] == 2:
                if len(a[0]) > 1:
                    if len(a[1]) > 1:
                        return f"({a[0]}) {a[2]} ({a[1]})"
                    else:
                        return f"({a[0]}) {a[2]} {a[1]}"
                else:
                    if len(a[1]) > 1:
                        return f"{a[0]} {a[2]} ({a[1]})"
                    else:
                        return f"{a[0]} {a[2]} {a[1]}"
            else:
                if a[2] == '-':
                    if len(a[1]) > 1:
                        if a[1][0] == '(':
                            return f"{a[0]} {a[2]} {a[1]}"
                        else:
                            return f"{a[0]} {a[2]} ({a[1]})"
                    else:
                        return f"{a[0]} {a[2]} {a[1]}"
                return f"{a[0]} {a[2]} {a[1]}"


def pre_to_i(prefix):
    if len(prefix) < 3:
        return "Invalid expression"
    if prefix[0] not in operators:
        return "Invalid expression"
    a = prefix.strip().split()
    i = 0
    while i < len(a)-2:
        try:
            if operators[a[i]]:
                if a[i+1] not in operators and a[i+2] not in operators:
                    a[i] = f"{a[i+1]} {a[i+2]} {a[i]}"
                    del a[(i+1):(i+3)]
                    i = 0
                else:
                    i += 1
            else:
                i += 1
        except KeyError:
            i += 1
    return post_to_i(' '.join(a))


def calc(expr, mode=None):
    if mode == 'postfix':
        try:
            return eval(post_to_i(expr))
        except SyntaxError:
            return f"Invalid expression"
    elif mode == 'prefix':
        try:
            return eval(pre_to_i(expr))
        except SyntaxError:
            return f"Invalid expression"

#print(calc('10 1 - 5 2 - 7 ** / 5 ** 3 7 ** 2 5 - - *', 'postfix'))


def pre_to_post(prefix):
    if len(prefix) < 3:
        return "Invalid expression"
    if prefix[0] not in operators:
        return "Invalid expression"
    a = prefix.strip().split()
    i = 0
    while i < len(a) - 2:
        try:
            if a[i + 1] not in operators and a[i + 2] not in operators:
                a[i] = f"{a[i + 1]} {a[i + 2]} {a[i]}"
                del a[(i+1):(i + 3)]
                i = 0
            else:
                i += 1
        except KeyError:
            i += 1
    if len(a) > 1:
        return "Invalid expression"
    else:
        return a[0]


def post_to_pre(postfix):
    if len(postfix) < 3:
        return "Invalid expression"
    if not postfix[0].isalnum():
        return "Invalid expression"
    ps = postfix.strip().split()
    i = 0
    while i < len(ps) - 2:
        try:
            if ps[i] not in operators and ps[i+1] not in operators:
                if operators[ps[i+2]]:
                    ps[i] = f'{ps[i+2]} {ps[i]} {ps[i+1]}'
                    del ps[(i+1):(i+3)]
                    i -= 1
            else:
                i += 1
        except KeyError:
            i += 1
    if len(ps) > 1:
        return "Invalid expression"
    return ps[0]
