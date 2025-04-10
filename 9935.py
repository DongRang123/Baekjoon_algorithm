T = input()
bomb = input()


def check(stack):
    #폭탄 인지 확인하고 다시 집어넣기 용 스택
    temp_stack = []
    idx = -1
    while idx != -len(bomb)-1:
        strs = stack.pop()
        temp_stack.append(strs)
        if strs == bomb[idx]:
            idx -= 1
        else:
            for z in temp_stack[::-1]:
                stack.append(z)
            break
    return stack

#저장 스택
check_stack = []

for i in T:
    check_stack.append(i)
    if len(check_stack)>=len(bomb) and check_stack[-1] == bomb[-1]:
        check_stack = check(check_stack)



if not check_stack:
    print('FRULA')
else:
    print(''.join(check_stack))