T= int(input())
for test_case in range(1,T+1):
    N= int(input())
    array= list(map(int,input().split()))
    array.sort()    
    print(f'#{test_case}',end=' ')
    print(*array)
