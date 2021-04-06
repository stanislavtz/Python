collection = []
n = int(input())

for i in range(n):
    collection.append(input())

searched_letter = ''
letters_dict = {}
counter = 0
for line in collection:
    for letter in line:
        if not letter in letters_dict:
            letters_dict[letter] = 0
        letters_dict[letter] += 1

searched_letter = sorted(letters_dict, key=lambda x: letters_dict[x], reverse=True)[0]

sequence = searched_letter

result = [sequence]

for i in range(1, n):
    current_occur = collection[i].count(searched_letter)
    if current_occur >= len(sequence) + 2:
        sequence = (len(sequence) + 2) * searched_letter
        result.append(sequence)

[print(seq) for seq in result]