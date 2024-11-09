T= int(input())
daylist = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,9:30,10:31,11:30,12:31}
for test_case in range(1, T+1):
    answer=1
    month_a , day_a , month_b, day_b = map(int,input().split())
    for _ in range(month_a,month_b):
        answer+=daylist[_]
    answer= answer-day_a+day_b
    print(f'#{test_case} {answer+1}')
