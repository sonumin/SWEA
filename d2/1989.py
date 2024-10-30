N =int(input())

for i in range(1,N+1):
    K=input()
    if(K!=K[::-1]):
        print(f'#{i} 0')
    else:
        print(f'#{i} 1')
