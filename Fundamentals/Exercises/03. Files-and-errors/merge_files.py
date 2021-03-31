with open('./merge_files/first.txt', 'r') as first_f:
    f_list = first_f.readlines()
    f_list[-1] += '\n'

    with open('./merge_files/second.txt', 'r') as second_f:
        s_list = second_f.readlines()
        merged = f_list + s_list
        
        with open('./merge_files/output.txt', 'w') as output_f:
            output_f.writelines(merged)