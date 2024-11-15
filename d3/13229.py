T= int(input())
dic = {'MON':1,'TUE':2,'WED':3,'THU':4,'FRI':5,'SAT':6,'SUN':0}
for test_case in range(1,T+1):
    today = input()
    answer = 7-dic[today]
    print(f'#{test_case} {answer}')