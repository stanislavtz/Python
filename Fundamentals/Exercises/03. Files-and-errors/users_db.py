import json

path = './user_database/users.txt'

def get_user(username, users_list):
    u_l = list(filter(lambda u: u['username'] == username, users_list))

    if len(u_l) == 0:
        return None

    return u_l[0]

def register_user(user):
    with open(path, 'a') as u_db:
        u_db.write(json.dumps(user)+'\n')


def save_users_status(users):
    with open(path, 'w') as u_db:
        [u_db.write(json.dumps(user)+'\n') for user in users]


data = input()
while data != 'exit':
    command = data.split()[0]
    username = data.split()[1]

    with open(path, 'r') as u_db:
        users = u_db.readlines()

    users_list = list(map(lambda u: json.loads(u), users))

    user = get_user(username, users_list)

    if command == 'register':
        password = data.split()[2]
        re_password = data.split()[3]

        if user:
            print('The given username already exists.')
            data = input()
            continue

        if password != re_password:
            print('The two passwords must match.')
            data = input()
            continue

        new_user = {}
        new_user['username'] = username
        new_user['password'] = password
        new_user['logged_in'] = False

        register_user(new_user)
    elif command == 'login':
        password = data.split()[2]

        if not user:
            print('There is no user with the given username.')
        elif user['password'] != password:
            print('The password you entered is incorrect.')
        else:
            if user['logged_in']:
                print(f'{user["username"]} is already logged in.')
                data = input()
                continue
            user['logged_in'] = True
            save_users_status(users_list)
    elif command == 'logout':
        if not user['logged_in']:
            print(f'{user["username"]} is not currently logged in.')
            data = input()
            continue

        user['logged_in'] = False
        save_users_status(users_list)

    data = input()