T= int(input())
answer_dic = {'p':'q','q':'p','b':'d','d':'b'}

for test_case in range(1,T+1):
    K = input()
    fact_answer=''
    answer=K[::-1]
    for i in answer:
        fact_answer +=answer_dic[i]
    print(f'#{test_case} {fact_answer}')
