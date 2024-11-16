T= int(input())

for test_case in range(1,T+1):
    N= int(input())
    numList = list(map(int,input().split()))
    cnt=0
    for i in range(1,N-1):
        if numList[i-1] < numList[i] < numList[i+1] or numList[i-1] > numList[i] > numList[i+1]:
            cnt+=1
        else:
            continue
    print(f'#{test_case} {cnt}')