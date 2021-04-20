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
    pattern = r'^\d+[A-Za-z]{num}[^A-Za-z]*$'
    ptrn = pattern.format(num='{'+str(num)+'}')
    match = re.match(ptrn, string)
    
    if match:
        for i in range(len(string)):
            if not string[i].isdigit():
                index = i
                break
        
        left_code_indexes = string[:index]
        message = string[index:index+num]
        right_code_indexes = string[index+num:]

        v_l = []

        v_l = append_char(message, left_code_indexes, v_l)
        v_l = append_char(message, right_code_indexes, v_l)

        vertification_code = ''.join(v_l)

        print(f"{message} == {vertification_code}")
    

    string = input()