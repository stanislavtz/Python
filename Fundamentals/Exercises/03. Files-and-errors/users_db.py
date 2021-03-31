import json

path = './user_database/users.txt'

def register_user(user):
    with open(path, 'a') as u_db:
        u_db.write(json.dumps(user)+'\n')

def login_user(users):
    with open(path, 'w') as u_db:
        [u_db.write(user) for user in users]

data = input()
while data != 'exit':
    command = data.split()[0]
    
    with open(path, 'r') as u_db:
        users = u_db.readlines()
 
    if command == 'register':
        username = data.split()[1]
        password = data.split()[2]
        re_password = data.split()[3]
        user = {}
        
        mapped = map(lambda u: json.loads(u)['username'], users)
        
        if username in mapped:
            print('The given username already exists.')
            data = input()
            continue
    
        if password != re_password:
            print('The two passwords must match.')
            data = input()
            continue
        
        user['username'] = username
        user['password'] = password
        user['logged_in'] = False

        register_user(user)
    elif command == 'login':
        username = data.split()[1]
        password = data.split()[2]

        user_list = [user for user in users if json.loads(user)['username'] == username]
        s_user = user_list[0] if len(user_list) > 0 else None
        
        if not s_user:
            print('There is no user with the given username.')
        elif json.loads(s_user)['password'] != password:
            print('The password you entered is incorrect.')
        else:
            if json.loads(s_user)['logged_in'] == False:
                index = users.index(s_user)
                users[index] = s_user.replace('false', 'true')

                login_user(users)
            else:
                s_user = [user for user in users if 'true' in user][0]
                if s_user:
                    print('There is already a logged in user.')
    elif command == 'logout':
        s_user = [user for user in users if 'true' in user][0]
        if not s_user:
            print('There is no currently logged in user.')

    data = input()