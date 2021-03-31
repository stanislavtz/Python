with open('./odd_lines/input.txt', 'r') as f:
    lines = f.readlines()
    with open('./odd_lines/output.txt', 'w') as new_f:
        [new_f.write(line) for index, line in enumerate(lines) if index % 2 == 1]