# 테스트 케이스 수 입력
T = int(input())

for test_case in range(1, T + 1):
    # 카드의 개수 입력
    N = int(input())
    # 카드 리스트 입력
    cards = input().split()
    
    # 절반으로 나누기
    mid = (N + 1) // 2  # 홀수일 경우 첫 번째 덱이 한 장 더 많음
    first_half = cards[:mid]
    second_half = cards[mid:]
    
    # 퍼펙트 셔플 결과 저장할 리스트
    shuffled = []
    
    # 교대로 카드 합치기
    for i in range(mid):
        shuffled.append(first_half[i])
        if i < len(second_half):  # 두 번째 덱에 카드가 남아 있을 경우
            shuffled.append(second_half[i])
    
    # 결과 출력
    print(f"#{test_case} {' '.join(shuffled)}")
