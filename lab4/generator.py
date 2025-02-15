#1
def generat(N):
    for i in range(1, N + 1):
        yield i ** 2
        
        
N = int(input())
for square in generat(N):
    print(square)
    
    
#2
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield str(i)
n = int(input())
print(", ".join(even_numbers(n)))


#3
def divis(M):
    for i in range(M + 1):
        if i % 3 == 0 and i % 4 ==0:
            yield i
M = int(input())
print(list(divis(M)))

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = int(input())
b = int(input())
print("squares: ")
for square in squares(a, b):
    print(square)


#5
def gena(m):
    for i in range(m, -1, -1):
        yield i
m = int(input())
for num in gena(m):
    print(num)
