def filter_uppercase(in_symbol):
    return in_symbol.isupper()


input_string = input()
i = int(input())
j = int(input())

out_filter = filter(filter_uppercase, input_string[i - 1:j])
print(len(list(out_filter)))
