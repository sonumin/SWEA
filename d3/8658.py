T = int(input())

for test_case in range(1,T+1):
    sum_list = list(map(str,input().split()))

    print(sum_list)
    answer=[]
    for number in sum_list:
        sum=0
        for j in range(len(number)):
            sum+=int(number[j])
        answer.append(sum)
    print(f'#{test_case} {max(answer)} {min(answer)}')