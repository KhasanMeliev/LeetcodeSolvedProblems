def func(s):
    stack = []
    curr, sign = 0, '+'
    for c in s+'+':
        if c==' ':
            continue
        elif c.isdigit():
            curr=(curr*10)+int(c)
        else:
            if sign=='+':
                stack.append(curr)
            elif sign=='-':
                stack.append(-curr)
            elif sign =='*':
                stack.append(stack.pop()*curr)
            else:
                stack.append(stack.pop()//curr)
                print(stack, curr)
            curr,sign=0,c

    return stack

print(func(" 3+5 / 2"))