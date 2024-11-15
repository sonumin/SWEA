for test_case in range(10):
    number = int(input())
    A,B = map(int,input().split())
    answer = pow(A,B)

    print(f'#{number} {answer}')