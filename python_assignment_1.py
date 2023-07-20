def character_check(paswd):
    special_character = ['+','-','*','&','%','$','#','@','!','?']
    for i in special_character:
        if (paswd == i ):
            return True
    return False

def check_password_strength(password, value, list1):
    uppercase, lowercase, digit, character, i = 0, 0, 0, 0, 0
    length = int(len(password))
        
    if (length>=8):
        for i in range (0, length):
            if (password[i].isupper()):
                uppercase += 1
            elif(password[i].islower()):
                lowercase += 1
            elif(password[i].isdigit()):
                digit += 1
            elif(character_check(password[i]) == True):
                character +=1

        value = (uppercase != 0 and lowercase != 0 and digit != 0 and character != 0)
        # print(uppercase, lowercase, digit, character)
        list1.append(uppercase)
        list1.append(lowercase)
        list1.append(digit)
        list1.append(character)
        list1.append(value)

    return list1

value = False
list1 = []
pwsd = input('Enter your password : ')
list2 = check_password_strength(pwsd, value, list1)

if (len(list2)>0):  
    uppercase = list2[0]
    lowercase = list2[1]
    digit = list2[2]
    character = list2[3]
    criteria = list2[4]

    if (criteria == True):
        print('Entered password meets the criteria and password is strong.')
    else:
        message = 'Entered password does not meet the criteria.'
        if (uppercase == 0):
            print(message, 'Missing an uppercase in password.')
        elif(lowercase == 0):
            print(message, 'Missing a lowercase in password.')
        elif(digit == 0):
            print(message, 'Missing a digit in password.')
        elif(character == 0):
            print(message, 'Missing a special character input in password.')
else:
    print('Password should be of atleast 8 characters.')