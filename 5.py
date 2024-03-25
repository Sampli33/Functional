import functools

a = int(input())
b = int(input())
c = int(input())

multiplying_list = [x for x in range(a, b+1) if int(x**0.5) ** 2 == x and x % c == 0]
out_multiplying = functools.reduce(lambda x, y: x * y, multiplying_list)
print(out_multiplying)
