T= int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split(' '))
    arr=[0]*N
    for num in range(N):
        arr[num]= list(map(int,input().split(' ')))
    max_number=0
    print(arr)
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt=0
            for x in range(i,i+M):
                for y in range(j,j+M):
                    cnt +=arr[x][y]
                if max_number<cnt:
                    max_number=cnt
    print(f'#{test_case} {max_number}')
            