for case in range(1, 11):
    N, M = input().split()
    x = list(M)
    stack = []
    for i in x: # 비밀번호에 대해
        if len(stack) == 0: # 스텍의 길이가 0이면
            stack.append(i) # 스택에 추가
        else:
            if stack[-1] == i: # 스택의 마지막 요소와 현재 x의 값이 같으면
                stack.pop() # 스택의 마지막 요소 제거
            else:
                stack.append(i) # 마지막과 다르면 스택에 추가
    print(f'#{case}',' ',*stack,sep='')