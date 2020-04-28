import random
import time
from sys import exit
again = "yes"
while again =="yes":
    if again == "no":
        exit(0)
    password_length = int(input("Enter the length of the password: "))
    while(not((password_length >= 12)and(password_length <= 25))):
        password_length = int(input("Enter the length of the password: "))
    possible_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=?><:'{}[]|1234567890"
    random_character_list = [random.choice(possible_characters) for i in range(password_length)]

    random_password = "".join(random_character_list)
    print(random_password)
    again = input("would u like continue? yes/no")
