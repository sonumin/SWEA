T= int(input())

for test_case in range(1,T+1):
    N= int(input())
    money=[50000,10000,5000,1000,500,100,50,10]
    K=[0]*len(money)
    for i in range(len(money)):
        if( N // money[i] > 0):
            K[i]+= N//money[i]
            N %=money[i]
    print(f'#{test_case}')
    print(*K)    