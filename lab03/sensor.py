porog = float(input())
n = int(input())

v = n
errors = 0

for i in range(n):
    s = input()
    if s == "error":
        errors = errors + 1
    else:
        t = float(s)
        # тут будет логика

