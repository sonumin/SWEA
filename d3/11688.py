T= int(input())

for test_case in range(1,T+1):
    word = input()
    A=1
    B=1
    for i in word:
        if i=='L':
            B+=A
        if i=='R':
            A+=B
    print(f'#{test_case} {A} {B}')