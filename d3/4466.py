T= int(input())

for test_case in range(1,T+1):
    N, K = map(int,input().split()) #4 #2
    score_list = list(map(int,input().split()))
    score_list.sort(reverse=True)
    print(score_list)
    total =0
    for i in range(K):
        total+=score_list[i]
    print(f'#{test_case} {total}')