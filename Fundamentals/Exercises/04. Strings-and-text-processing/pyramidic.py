# n = int(input())
# collection = []
# result = []

# for i in range(n):
#     collection.append(input())

# searched_letter = None
# for i in range(n):
#     for letter in collection[i]:
#         if collection[i].count(letter) >= 2*(i+1) - 1:
#             searched_letter = letter
#     result.append(searched_letter)   

# print(result)

n = int(input())
text = ''

for i in range(n):
    text += input() + ' '

text = text.strip()
letter_occurs = 0
searched_letter = ''

for letter in text:
    counter = text.count(letter)
    if counter > letter_occurs:
        letter_occurs = counter
        searched_letter = letter

text_list = text.split(' ')
searched_text = []

for string in text_list:
    if searched_letter in string:
        num_occurs = string.count(searched_letter)
        searched_text.append(num_occurs * searched_letter)

searched_text.sort()
i = 1
for item in searched_text:
    if item.count(searched_letter) >= i:
        print(searched_letter * i)
        i += 2
