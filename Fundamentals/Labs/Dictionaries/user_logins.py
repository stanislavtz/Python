db = {}

data = input()
while data != 'login':
    username = data.split(' -> ')[0]
    password = data.split(' -> ')[1]
    db[username] = password
    data = input()

counter = 0
data = input()
while data != 'end':
    username = data.split(' -> ')[0]
    password = data.split(' -> ')[1]
    
    if not username in db.keys() or db[username] != password:
        print(F"{username}: login failed")
        counter += 1
        data = input()
        continue
    
    print(f"{username}: logged in successfully")

    data = input()

print(f"unsuccessful login attempts: {counter}")