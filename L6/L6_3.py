def get_digits(x):
    x = str(x)
    return tuple([int(c) for c in x])



print(get_digits(87178291199))