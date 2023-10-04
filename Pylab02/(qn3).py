P= int(input())
X= int(input())
i=1
j=1
for i in range (P+1):
    for j in range (i+1):
        if j==P-i and j^i==X:
            print(j,i,end=" ")
    i+=1
    j+=1