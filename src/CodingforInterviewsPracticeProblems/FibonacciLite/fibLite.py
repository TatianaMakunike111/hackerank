n = int(input().strip())

fib_0, fib_1 = 0, 1
for _ in range(n):
    fib_0, fib_1 = fib_1, fib_0 + fib_1

print(fib_0)
