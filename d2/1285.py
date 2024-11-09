T= int(input())

for test_case in range(1,T+1):
    N= int(input())
    distances = list(map(int,input().split()))
    min_distance=100001
    cnt=0
    for i in range(N):
        if(abs(distances[i])<=min_distance):
            min_distance= distances[i]
    for _ in range(N):
        if(abs(distances[_])==min_distance):
            cnt+=1
    print(f'#{test_case} {min_distance} {cnt}')