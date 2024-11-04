T = int(input())
for i in range(1, T + 1):
    _ = input()
    grades = list(map(int, input().split()))
    freq = [0] * 101 
    mode = 0

    for grade in grades:
        freq[grade] += 1
        if freq[grade] >= freq[mode]:
            mode = grade

    print(f'#{i} {mode}')
