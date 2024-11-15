T= int(input())

for test_case in range(1,T+1):
    student_score = list(map(int,input().split()))
    sum=0
    for i in student_score:
        if i<40:
            sum+=40
        else:
            sum+=i
    answer=sum/len(student_score)
    print(f'#{test_case} {int(answer)}')