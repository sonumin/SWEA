T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    sum_arr = []
    
    # 각 행의 합 계산
    for row in range(100):
        row_sum = sum(arr[row])
        sum_arr.append(row_sum)
    
    # 각 열의 합 계산
    for column in range(100):
        col_sum = 0
        for row in range(100):
            col_sum += arr[row][column]
        sum_arr.append(col_sum)
    
    # 첫 번째 대각선 (왼쪽에서 오른쪽)
    diag1_sum = 0
    for i in range(100):
        diag1_sum += arr[i][i]
    sum_arr.append(diag1_sum)
    
    # 두 번째 대각선 (오른쪽에서 왼쪽)
    diag2_sum = 0
    for i in range(100):
        diag2_sum += arr[i][99-i]
    sum_arr.append(diag2_sum)
    
    # 결과 계산: 최댓값 구하기
    answer = max(sum_arr)
    
    print(f'#{test_case} {answer}')
