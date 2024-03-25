num = 10

a, b = 1, 1
print(a, end=" ")
print(b, end=" ")


for _ in range(2, num):
    c = a + b
    print(c, end=" ")
    a, b = b, c
