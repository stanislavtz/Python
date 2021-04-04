words, text = input().split(), input()

for word in words:
    text = text.replace(word, '*'*len(word))
    
print(text)