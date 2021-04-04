def rotate(destination, times, string):
    cicles = times % len(string)
    for i in range(cicles):
        if destination == 'Left':
            string = string[1:] + string[0]
        elif destination == 'Right':
            string = string[-1] + string[:-1]
    return string


string, command_line = input(), input()

while command_line != 'end':
    command = command_line.split()[0]

    if command == 'Left' or command == 'Right':
        string = rotate(command, int(command_line.split()[1]), string)
    elif command == 'Insert':
        index = int(command_line.split()[1])
        str_to_insert = command_line.split()[2]
        string = string[:index] + str_to_insert + string[index:]
    elif command == 'Delete':
        start_index = int(command_line.split()[1])
        end_index = int(command_line.split()[2])
        string = string[:start_index] + string[end_index+1:]
    
    command_line = input()

print(string)