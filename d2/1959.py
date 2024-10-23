T= int(input())

for i in range(1,T+1):
    a,b= map(int,input().split())
    numA= list(map(int,input().split()))
    numB=list(map(int,input().split()))
    max=0
    if(a>b):
        a,b=b,a
        numA,numB=numB,numA

    for k in range(b-a+1):
        temp=0
        for j in range(a):
            temp+=numA[j]*numB[j+k]
        if temp>max:
            max=temp
    print(f"#{i} {max}")