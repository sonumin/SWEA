T= int(input())

for test_case in range(1,T+1):
    N= int(input())
    arr = list(map(int,input().split(' ')))
    print(arr)
    answer=0
    max_number=0
    for pivot in arr[::-1]:
        print(pivot)
        if pivot>=max_number:
            max_number=pivot
        else:
            answer += max_number - pivot
    print(f"#{test_case} {answer}")
