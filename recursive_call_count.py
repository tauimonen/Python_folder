

def f(n):
    f.count += 1
    if n <= 2:
        return n
    return f(n-1)+f(n-2)+f(n-3)

f.count = 0
n = 30
f(n)
print(f.count)
