with open('./line_numbers/input.txt', 'r') as f:
    lines = f.readlines()
    
    with open('./line_numbers/output.txt', 'w') as new_f:
        [new_f.writelines(f'{index+1}. {line}') for index, line in enumerate(lines)]