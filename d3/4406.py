T= int(input())

for test_case in range(1,T+1):
    word = input()
    m_list = ['a','e','i','o','u']
    for i in m_list:
        word=word.replace(i,'')
    print(f'#{test_case} {word}')