from timeit import default_timer as timer

def f(n):
    if n <= 2:
        return n
    return f(n-1)+f(n-2)+f(n-3)

if __name__ == "__main__":
    n = 30
    start = timer()
    res = f(n)
    end = timer()
    print(res)
    print("Aikaa kului:", end - start, " s")