def map_l7(func_map, items:list):
    x = [func_map(a) for a in items]
    return x

print(map_l7(lambda x: x**2, (1,2,3,4,5,6,7,8,9)))
