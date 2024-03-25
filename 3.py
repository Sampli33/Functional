a = int(input())
b = int(input())
c = int(input())
d = int(input())

out_filter = list(map(lambda x: x % c != 0 and x % 10 == d,
                      range(a, b+1)))
print(sum(out_filter))
