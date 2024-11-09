T= int(input())

for test_case in range(1,T+1):
    N= int(input())
    answer=''
    for n_case in range(N):
        alpha, cnt = input().split()
        answer+=alpha*int(cnt)
    print(f'#{test_case}')    
    for i in range(0,len(answer),10):
        print(answer[i:i+10])
