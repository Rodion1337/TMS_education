x = ('roTaTor', 'Class', 'noOn', 'python', 'летел', 'каБак', 'ищи')

x = [c if c.islower() else c.lower() for c in x]

print(list(filter(lambda c : c == c[::-1], x)))
