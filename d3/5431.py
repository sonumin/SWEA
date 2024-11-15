T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    K_list = list(map(int, input().split()))
    students = list(map(int, range(1, N + 1)))
    result = []
    for j in students:
        if j not in K_list:
            result.append(j)
    print(f'#{i}', end=" ")
    print(*result)