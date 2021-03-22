import re

data = input()
words = re.findall(r"\w+#", data)
lower_case = []
mixed_case = []
upper_case = []

for word in words:
    if re.match(r"[a-z]+", word):
        lower_case.append(word)
    elif re.match(r"[A-Z]+[^a-z]+", word) and word != 'C#':
        upper_case.append(word)
    else:
        mixed_case.append(word)
    

print(f"Lower-case: {', '.join(lower_case)}")
print(f"Mixed-case: {', '.join(mixed_case)}")
print(f"Upper-case: {', '.join(upper_case)}")