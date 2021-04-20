import re


def append_char(message, indexes, vertification_list):
    for  char in indexes:
        try:
            vertification_list.append(message[int(char)])
        except:
            vertification_list.append(' ')
        
    return vertification_list
            


string = input()

while string != 'Over!':
    num = int(input())
    pattern = r'\d+[A-Za-z]+{num}[^A-Za-z]+'
    ptrn = pattern.format(num='{'+str(num)+'}')
    match = re.match(ptrn, string)
    print(match)
    if match:
        p = r'[A-Za-z]+'
        split_arg = re.match(p, match.string)
        code_indexes = string.split(split_arg)
        message = string[num:num*2]
        
        v_l = []

        v_l = append_char(message, code_indexes[0], v_l)
        v_l = append_char(message, code_indexes[1], v_l)

        vertification_code = ''.join(v_l)

        print(f"{message} == {vertification_code}")
    

    string = input()