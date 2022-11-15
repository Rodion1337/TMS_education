def sum_list(list_to_sum):
    return [sum(list_to_sum) - list_to_sum[x] for x in range(0, len(list_to_sum))]