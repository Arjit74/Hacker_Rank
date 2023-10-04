n= int(input())
for i in range(1,n+1):
    a= bin(i)[2:]
    print(f"{a:<>{len(bin(n))-2}}")