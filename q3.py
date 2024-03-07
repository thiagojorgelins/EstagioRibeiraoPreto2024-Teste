# - a) 1, 3, 5, 7, __= 9
# - b) 2, 4, 8, 16, 32, 64, __= 128
# - c) 0, 1, 4, 9, 16, 25, 36, __= 49
# - d) 4, 16, 36, 64, __ =100
# - e) 1, 1, 2, 3, 5, 8, __ =13
# - f) 2, 10, 12, 16, 17, 18, 19, __= 200 números que começam com a letra D

a = [i for i in range(10) if i % 2 != 0]
print(f'Resposta letra a) {a[len(a)-1]}')

b = [2**i for i in range(1,8)]
print(f'Resposta letra b) {b[len(b)-1]}')

c = [i**2 for i in range(8)]
print(f'Resposta letra c) {c[len(c)-1]}')

d = []
x = 4
aux = 12
while x < 120:
    d.append(x)
    x += aux
    aux += 8
print(f'Resposta letra d) {d[len(d)-1]}')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
e = [fib(i) for i in range(8)]
print(f'Resposta letra f) {e[len(e)-1]}')

f = print('Resposta letra f) 200 - Números que começam com a letra D')