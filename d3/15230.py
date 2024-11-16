T= int(input())

for test_case in range(1,T+1):
    default = 'abcdefghijklmnopqrstuvwxyz'
    inp = input()
    answer=0
    for i in range(0,len(inp)):
        if(default[i]!=inp[i]):
            answer=i
            break
    print(f'#{test_case} {i}')
    