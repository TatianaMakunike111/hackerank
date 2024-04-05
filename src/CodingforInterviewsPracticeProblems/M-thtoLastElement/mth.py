M = int(input().strip())
L = list(map(int, input().strip().split()))

if M <= 0 or M > len(L):
    print("NIL")
else:
    print(L[-M])