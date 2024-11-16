T= int(input())

for test_case in range(1,T+1):
    N, A, B = map(int,input().split())

    
    min_num= min(A,B)
    max_num=0
    if N-A-B>0:
        max_num= 0
    else:
        max_num= abs(N-A-B)
    print(f'#{test_case} {min_num} {max_num}')