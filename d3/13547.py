T= int(input())

for test_case in range(1,T+1):
    now_list = list(map(str,input()))
    print(now_list)
    if(15-len(now_list)+now_list.count('o')>=8):
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')