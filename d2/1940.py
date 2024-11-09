T= int(input())

for test_case in range(1, T+1):
    N= int(input())
    distance=0
    now_ms=0
    for com_number in range(N):
        arr= list(map(int,input().split()))
        if(arr[0]==1):
            now_ms+=arr[1]
            distance+= now_ms
        if(arr[0]==0):
            distance+= now_ms
        if(arr[0]==2):
            if(now_ms<arr[1]):
                now_ms=0
                distance+= now_ms
            else:
                now_ms-=arr[1]
                distance+=now_ms
    print(f'#{test_case} {distance}')