import random

def gen_password():
    password = []
    counter = 0
    while True:
        num = random.random()
        if num >= 0 and num < 0.5:
            if num < 0.1:
                password.append(create_password(1))
            elif num >= 0.1 and num < 0.2:
                password.append(create_password(2))
            elif num >= 0.2 and num < 0.3:
                password.append(create_password(3))
            elif num >= 0.3 and num < 0.4:
                password.append(create_password(4))
            elif num >= 0.4 and num < 0.5:
                password.append(create_password(5))
        elif num >= 0.5:
            if num < 0.6:
                password.append(create_password(6))
            elif num >= 0.6 and num < 0.7:
                password.append(create_password(7))
            elif num >= 0.7 and num < 0.8:
                password.append(create_password(8))
            elif num >= 0.8 and num < 0.9:
                password.append(create_password(9))
            elif num >= 0.9 and num < 1:
                password.append(create_password(10))
        counter += 1
        if counter > 9:
            word = ""
            for i in password:
                word += str(i)
            return word
            break

def create_password(x):
    if x == 1 or x == 2:
        up_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'X', 'Y', 'Z']
        return random.choice(up_letter)
    elif x == 3 or x == 4:
        low_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'x', 'y', 'z']
        return random.choice(low_letter)
    elif x == 5 or x == 6:
        numbers_for = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        return random.choice(numbers_for)
    elif x == 7 or x == 8:
        numbers_back = [9,8,7,6,5,4,3,2,1,0]
        return random.choice(numbers_back)
    elif x == 9 or x == 10:
        special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '~', '`', '[', ']', '|',
                    '\'', ':', ';', ',', '.', '/', '?', '<', '>', '{', '}']
        return random.choice(special_char)

def crack_password(x):
    up_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'X', 'Y', 'Z']
    low_letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'x', 'y', 'z']
    numbers_for = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    special_char = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '~', '`', '[', ']', '|',
                    '\'', ':', ';', ',', '.', '/', '?', '<', '>', '{', '}']
    guess_password = []
    for sprite in x:
        if sprite.isdigit():
            for num in numbers_for:
                if num == int(sprite):
                    guess_password.append(num)
                    break
        elif sprite.isalpha():
            for letter in up_letter:
                if letter == sprite:
                    guess_password.append(letter)
                    break
            for l_letter in low_letter:
                if l_letter == sprite:
                    guess_password.append(l_letter)
                    break
        else:
            for char in special_char:
                if char == sprite:
                    guess_password.append(char)
                    break
    print("The secret password {} is comprised of these letters {}.".format(x,guess_password))


crack_password(gen_password())