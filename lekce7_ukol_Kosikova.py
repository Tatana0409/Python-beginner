def is_adult(age: int) -> bool:
    result = True if age >= 18 else False
    return result


def is_name_valid(name: str) -> bool:
    name_length = len(name)
    result = True if name_length >= 4 else False
    return result

#is_name_valid(name)


def create_user (name:str, age:int) -> dict:

    if is_adult(age) and is_name_valid(name):
        user = {
                'success': True,
                'user': {'username': name,
                         'age': age,
                         'email': name + '@gmail.com'
                         }
            }

    else: user = {
            'success': False,
            'error': 'Error message: Wrong Name or age!'
        }

    return user

def print_user_info(user: dict) -> None:
    print('Username:' + user['user']['username'])

# creation of users
users = []

user1 = create_user('loser5', 34)
users.append(user1)

user2 = create_user('upset', 11)
users.append(user2)

user3 = create_user('king', 45)
users.append(user3)

user4 = create_user('Tana', 34)
users.append(user4)

user5 = create_user('blabla', 45)
users.append(user5)

# print(users)
# nbr_users = len(users)
# print(nbr_users)

for x in users:
     if x ['success']:
         print_user_info(x)


