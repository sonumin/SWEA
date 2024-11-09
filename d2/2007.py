T= int(input())

for test_case in range(1,T+1):
    sentence= list(input())
    cnt=0
    for j in range(1,10):
        if sentence[0] != sentence[j] or sentence[1] != sentence[j+1]:
            cnt+=1
        else:
            break
    print(f'#{test_case} {cnt+1}')