T= int(input())

for test_case in range(1,T+1):
    K = input()
    dic=[]
    for i in K:
        if i not in dic:
            dic.append(i)
    print(f'#{test_case} {len(dic)}')