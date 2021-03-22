def read_inputs(n):
    my_list = []
    for _ in range(n):
        my_list.append(int(input()))
    return my_list

def sum_list_items(itter):
    return sum(itter)


n = int(input())
print(sum_list_items(read_inputs(n)))