st= str(input("Enter the rap line: "))
node= int(input(""))
rp= int(input())

out= st[node:]+st[:node]
rel=(out.replace(" ",""))*rp
print(*rel)