def generate_non_fibonacci(N):
   
    fib_set = {0, 1}
    a, b = 0, 1
    while b <= N:
        a, b = b, a + b
        fib_set.add(b)
    non_fib = [i for i in range(2, N + 1) if i not in fib_set]
    return non_fib

N = int(input())    

non_fibonacci = generate_non_fibonacci(N)

print(' '.join(map(str, non_fibonacci)))
