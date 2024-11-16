T = int(input())

for test_case in range(1, T+1):
    A, B, C = map(int,input().split())
    #A=빵 B= 빵 C = 현금
    select_bread=0
    if(A<B):
        select_bread=A
    else:
        select_bread=B
    answer=C//select_bread

    print(f'#{test_case} {answer}')