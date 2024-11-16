T= int(input())

for test_case in range(1,T+1):
    n,m =map(int,input().split())
    twin= n-m
    uni=m-twin
    print(f'#{test_case} {uni} {twin}')