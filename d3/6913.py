T= int(input())

for test_case in range(1,T+1):
    N,M = map(int,input().split())
    people= [list(map(int,input().split())) for _ in range(N)]
    people_score=[]
    for i in people:
        people_score.append(i.count(1))
    print(people_score)
    max_number=max(people_score)
    print(f'#{test_case} {people_score.count(max_number)} {max_number}')
