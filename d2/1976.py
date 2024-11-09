T= int(input())

for test_case in range(1,T+1):
    a,b,c,d = map(int,input().split())
    hour= a+c
    minute =b+d
    if(a+c>12):
        hour = (a+c)-12
    if(b+d>60):
        minute = (b+d)-60
        hour+=1
    print(f'#{test_case} {hour} {minute}')
