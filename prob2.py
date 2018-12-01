def fib(prev, curr, max_val, even_sum):
    if curr < max_val:
        if curr % 2 == 0:
            even_sum += curr

        fib(curr, curr+prev, max_val, even_sum)
    else:
        print(even_sum)

fib(0, 1, 4000000, 0)
