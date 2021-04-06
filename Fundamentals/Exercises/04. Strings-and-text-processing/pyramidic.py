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

result_lines_counter = 1
for i in range(n-1):
    current_occur = collection[i].count(searched_letter)
    next_occur = collection[i+1].count(searched_letter)
    if searched_letter in collection[i] and searched_letter in collection[i+1] and current_occur <= next_occur - 2:
        collection[i+1] = searched_letter * (current_occur + 2)
        result_lines_counter += 1

[print(searched_letter * (2*i - 1)) for i in range(1, result_lines_counter+1)]