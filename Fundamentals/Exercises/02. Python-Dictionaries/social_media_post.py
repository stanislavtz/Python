media, inp = {}, input()
while inp != 'drop the media':
    data = inp.split(' ', maxsplit=1)
    command, post = data[0], data[1]

    if command == 'post':
        if not post in media:
            media[post] = {
                'likes': 0, 'dislikes': 0, 'comments': []
            }
    elif command == 'like':
        if post in media:
            media[post]['likes'] += 1
    elif command == 'dislike':
        if post in media:
            media[post]['dislikes'] += 1
    elif command == 'comment':
        post, author, content = \
            data[1].split(' ', maxsplit=2)[0], data[1].split(' ', maxsplit=2)[1], data[1].split(' ', maxsplit=2)[2]

        media[post]['comments'].append((author, content))
    inp = input()

for post, obj in media.items():
    print(f"Post: {post} | Likes: {obj['likes']} | Dislikes: {obj['dislikes']}\nComments:")
    if len(obj['comments']) > 0:
        for comment in obj['comments']:
            print(f"*  {comment[0]}: {comment[1]}")
    else:
        print('None')