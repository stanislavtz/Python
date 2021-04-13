class User:
    def __init__(self, name):
        self.name = name
        self.received_msgs = []
    
class Message:
    def __init__(self, sender_name, content):
        self.sender_name = sender_name
        self.content = content

registered_users = []

data = input()
while data != 'exit':
    if data.split()[0] == 'register':
        name = data.split()[1]
        user = User(name)
        registered_users.append(user)
    else:
        sender_name, _, recipient_name, content = data.split()
        try:
            sender = list(filter(lambda u: u.name == sender_name, registered_users))[0]
            recipient = list(filter(lambda u: u.name == recipient_name, registered_users))[0]

            message = Message(sender.name, content)
            recipient.received_msgs.append(message)
        except: 
            data = input()
            continue

    data = input()

person_1_name, person_2_name = input().split()

if len(registered_users) == 0:
    print("No messages")
else:
    try:
        p1 = list(filter(lambda p: p.name == person_1_name, registered_users))[0]
        p2 = list(filter(lambda p: p.name == person_2_name, registered_users))[0]
       
        p1_to_p2 = list(filter(lambda m: m.sender_name == person_1_name, p2.received_msgs))
        p2_to_p1 = list(filter(lambda m: m.sender_name == person_2_name, p1.received_msgs))
        zipped_messages = list(zip(p1_to_p2, p2_to_p1))
        
        [print(f"{a[0].sender_name}: {a[0].content}\n{a[1].content} :{a[1].sender_name}") for a in zipped_messages]
        
        min_length = min(len(p1_to_p2), len(p2_to_p1))
       
        if len(p1_to_p2) == 0 and len(p2_to_p1) == 0:
            print("No messages")
        elif len(p1_to_p2) > len(p2_to_p1):
            [print(f"{m.sender_name}: {m.content}") for m in p1_to_p2[min_length:]]
        else:
            [print(f"{m.content} :{m.sender_name}") for m in p2_to_p1[min_length:]]

    except:
        print("No messages")
