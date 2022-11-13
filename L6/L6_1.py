def dict_key_item_reversed(dict0):
    dict_rev = {v: k for k, v in dict0.items()}
    return(dict_rev)

dict_no_rev = {'имя': 'Гадя','отчество':'Петрович','фамилия':'Хренова'}
dict_revers = dict_key_item_reversed(dict_no_rev)
print('Before:', dict_no_rev)
print('After:',dict_revers)