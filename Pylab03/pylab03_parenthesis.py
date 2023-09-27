n = input("")
lst = []
for i in n:
    if i == '(': 
        lst.append(i)
    elif i == ')':  
        if len(lst) > 0 and lst[-1] == '(':
            lst.pop() 
        else:
            print("'False'")
            break
else:
    if len(lst) == 0:
        print("'True'")
    else:
        print("'False'")


rows= int(input())
pos= int(input())
for i in range(1,rows+1):
    for j in range(rows-i):
        print("#" ,end="")
    for j in range(2*i-1):
        if j==0 or j==2*i-2 or i == pos:
            print('*',end="")
        else:
            print("%",end="")
    print()