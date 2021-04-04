text, criteria = input(), input()
filtered = None

if criteria == 'LOWERCASE':
    filtered = list(filter(lambda x: x.islower(), text))
else:
    filtered = list(filter(lambda x: x.isupper(), text))

chars_values = [ord(char) for char in filtered]
print(f"The total sum is: {sum(chars_values)}")