i = int(input())
j = 2

while j <= i // j:
    if i % j == 0:
        print("not a prime")
        break
    j = j + 1

if j > i // j:
    print("prime")
