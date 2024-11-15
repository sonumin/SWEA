T= int(input())

for test_case in range(1,T+1):
    N= int(input())
    people_List = list(map(int,input().split()))
    Avg = sum(people_List) //N
    print(Avg)
    cnt=0
    for i in people_List:
        if(i<=Avg):
            cnt+=1
    print(f'#{test_case} {cnt}')