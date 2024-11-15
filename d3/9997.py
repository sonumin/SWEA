T= int(input())

for test_case in range(1,T+1):
    K = int(input())
    total_min = K *2
    hour = total_min//60
    minute = total_min%60

    print(f'#{test_case} {hour} {minute}')