T= int(input())

for test_case in range(1,T+1):
    num_list= list(map(int,input().split()))
    num_list.sort()
    if num_list[1] != num_list[0]:
        print(f'#{test_case} {num_list[0]}')
    else:
        print(f'#{test_case} {num_list[2]}')
