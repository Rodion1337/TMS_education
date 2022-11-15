def combine_dicts(*args):
    print(args,type(args))
    print(args[0],args[1], len(args))



dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

combine_dicts(dict_1, dict_2)