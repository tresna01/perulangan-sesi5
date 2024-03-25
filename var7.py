a = 1
b = 1
c = 1

for i in range (10) :
    a = b 
    b = c
    c = a + b 
    print (a, end = " ")
print ()