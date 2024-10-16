T = int(input())

for test_case in range(1,T+1):
    N=int(input())
    K=1
    sleepList=[0,1,2,3,4,5,6,7,8,9]
    while len(sleepList)!=0:
        current=N*K
        for i in str(current):
            if int(i) in sleepList:
                sleepList.remove(int(i))
        K+=1
    print(f'#{test_case} {N*(K-1)}')
