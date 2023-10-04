n1= int(input())
n2= int(input())
k= int(input())
an= n1&n2
o=n1|n2
xo= n1^n2
l=[an,o,xo]
if an>k:
    an=0
if o>k:
    o=0
if xo>k:
    xo=0
if an>=o and an>=xo:
    print(an)
elif o>=an and o>=xo:
    print(o)
else:
    print(xo)
#Other way to do more convenient


n1 = int(input())
n2 = int(input())
k = int(input())
an = n1 & n2
o = n1 | n2
xo = n1 ^ n2
max_an = 0
max_o = 0
max_xo = 0

# Check if each result is within the limit of k and update the maximum values accordingly
if an <= k:
    max_an = an
if o <= k:
    max_o = o
if xo <= k:
    max_xo = xo

# Find the maximum among the values that are within the limit of k
max_value = max(max_an, max_o, max_xo)
print(max_value)