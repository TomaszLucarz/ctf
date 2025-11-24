amount = input()
users = dict()
passwords = []

# input data and sort for mail, user dict and passwords list
for i in range(int(amount)):
    string = input()
    if '@cygnus' in string:
        user = string.split('@')[0]
        users[string] = (user[:len(user)-1])  # dict of mail, user
    else:
        passwords.append(string)

result=[]  # list for sorting
for mail, user in users.items():
    for password in passwords:
        if user in password:
            result.append([mail, password])

result.sort()  
for pair in result:
    print(''.join(pair))  # print final pairs

