from functools import reduce


def remove_spaces(collection):
    result = filter(lambda x: x != ' ', list(map(lambda x: x.strip(), collection.split())))
    return list(result)


li = reversed(input().split('|'))
list_with_nospaces = list(map(lambda x: remove_spaces(x), li))
result = reduce(lambda a, b: a + b, list_with_nospaces)
print(' '.join(result))