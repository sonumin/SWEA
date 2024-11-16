T= int(input())

for test_case in range(1,T+1):

    N = int(input())
    flag=0
    for i in range(1,10):
        for j in range(1,10):
            if i*j==N:
                flag=1
                break
            else:
                continue
    if(flag==1):
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')