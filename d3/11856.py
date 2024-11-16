T= int(input())

for test_case in range(1,T+1):
    s=list(input())
    s.sort()
    if s[0]!=s[3] and s[0]==s[1] and s[2]==s[3]:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')