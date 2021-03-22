data = input()
unwanted = ", ; : . ! ( ) \" \' / [ ] \\".split(' ')

for u in unwanted:
    data = data.replace(u, ' ')

words = list(map(lambda x: x.strip(), data.split()))

lower_case = []
mixed_case = []
upper_case = []

for word in words:
    if word.islower() and word.isalpha():
        lower_case.append(word)
    elif word.isupper() and word.isalpha():
        upper_case.append(word)
    else:
        mixed_case.append(word)

print(f"Lower-case: {', '.join(lower_case)}")
print(f"Mixed-case: {', '.join(mixed_case)}")
print(f"Upper-case: {', '.join(upper_case)}")