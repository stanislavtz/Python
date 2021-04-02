def insert_tag(collection, tag_name, tag_line):
    enum_col = enumerate(collection)
    for index, line in enum_col:
        if '</title>' in line and tag_name == 'title':
            collection.remove(line)
            collection.insert(index, tag_line)
            break
        elif '</body>' in line:
            lines.insert(index, tag_line)
            break


path = './html_contents/index.html'

with open(path, 'r') as html_file:
    lines = html_file.readlines()

    data = input()
    while data != 'exit':
        tag_name = data.split()[0]
        content = data.split(' ', maxsplit=1)[1]
        tag_line = f"\t<{tag_name}>{content}</{tag_name}>\n"

        insert_tag(lines, tag_name, tag_line)

        data = input()

    with open(path, 'w') as new_html:
        [new_html.write(line) for line in lines]