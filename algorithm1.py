# cho 1 dãy số 123456789
# chèn vào giữa các số 1 phép toán (+, - or none) để ra kết quả 100

string = "123456789"
result = 100

def solutions(n):
    base = "123456789"
    length = len(base) + 1
    out = []
    
    def solve(x,i):
        if i + 1 == length:
            if eval(x) == n:
                out.append(x.lstrip("+"))
            return
        for j in range(i + 1, length):
            solve(f'{x}+{base[i:j]}', j)
            solve(f'{x}-{base[i:j]}', j)
                
    solve("",0)
    
    return out

print(solutions(100))

# results
# 1+2+3-4+5+6+78+9
# 1+2+34-5+67-8+9
# 1+23-4+5+6+78-9
# 1+23-4+56+7+8+9
# 12+3+4+5-6-7+89
# 12+3-4+5+67+8+9
# 12-3-4+5-6+7+89
# 123+4-5+67-89
# 123+45-67+8-9
# 123-4-5-6-7+8-9
# 123-45-67+89
# -1+2-3+4+5+6+78+9
    
