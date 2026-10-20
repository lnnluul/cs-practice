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
        sum_t = summ_t + t
        
        if t > max_t:
            max_t = t
            
        if t > porog:
            p = p + 1

