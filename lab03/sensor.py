porog = float(input())
n = int(input())

v = n
errors = 0
p = 0
max_t = -1000.0 
sum_t = 0.0
cnt_t = 0

for i in range(n):
    s = input()
    if s == "error":
        errors = errors + 1
    else:
        t = float(s)

        cnt_t = cnt_t + 1
        sum_t = sum_t + t
        
        if t > max_t:
            max_t = t
            
        if t > porog:
            p = p + 1

if cnt_t > 0:            
    sr = sum_t / cnt_t
else:
    sr = 0.0

print(v)
print(errors)
print(p)
print("%.1f" % max_t)
print("%.1f" % sr)

