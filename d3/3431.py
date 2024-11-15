T= int(input())

for test_case in range(1,T+1):
    L, U, K =map(int,input().split())
    if K<L:
        print(f'#{test_case} {L-K}')
    elif K>=L and K<=U:
        print(f'#{test_case} {0}')
    else:
        print(f'#{test_case} {-1}')