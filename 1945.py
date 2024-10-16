N = int(input())
for tc in range(1,N+1):    
    K=int(input())
    numList= [2,3,5,7,11]
    cntList=[0,0,0,0,0]
    for i in range(5):
        while K % numList[i]==0:
            cntList[i]+=1
            K/=numList[i]
    print(f'#{tc}',end=' ')
    print(*cntList)