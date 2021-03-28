forum, data = {}, input()
while data != 'filter':
    topic, tags = data.split(' -> ')[0], data.split(' -> ')[1].split(', ') 

    if not topic in forum:
        forum[topic] = []
    forum[topic] += tags

    data = input()

filtered_forum, searched = {}, input().split(', ')

for topic, tags in forum.items():
    t_sorted = sorted(set(tags), key=tags.index)

    if set(searched).issubset(tags):
        filtered_forum[topic] = list(map(lambda x: f"#{x}", t_sorted))
            
print('\n'.join([f"{k} | {', '.join(v)}" for k, v in filtered_forum.items()]))