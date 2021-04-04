words = input().split()
palindromes = sorted(list(filter(lambda x: x == x[::-1], words)), key=str.lower)
result = sorted(set(palindromes), key=palindromes.index)
print(', '.join(result))