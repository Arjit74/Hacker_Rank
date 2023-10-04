index = int(input())
count = 0  
num = 1    
while count < index:
    if num % 3 != 0 and num % 3 != 3:
        count += 1
        if count == index:
            print(num)
    num += 1