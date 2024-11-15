T = int(input())

for test_case in range(1,T+1):
    K= int(input())
    
    if(K%2==0):
        print(f'#{test_case} Alice')
    else:
        print(f'#{test_case} Bob')