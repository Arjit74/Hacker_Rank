n= str(input())
l= len(n)
if l%2==0:
    a=n[:n:-1]+n[2:]
    print(a)
else:
    print("Odd length.")