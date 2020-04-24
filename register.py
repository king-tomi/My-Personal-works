import re
import random
import pprint

def catch_password(password):
    """A program that matches a password

       password: the string to be matched"""
    valid_password = re.compile(r"\w{7,}")
    if valid_password.search(password):
        return True
    else:
        return False


def catch_email(email):
    valid = re.compile(r"\w+\@\w+[.]\w+")
    if valid.search(email):
        return True
    return False


class User:
    """A User object to model a user registering"""

    def __init__(self,first_name,last_name,email,password):
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    def __repr__(self):
        return f"{self._first_name} {self._last_name}"

users = []

def register():
    """A function that registers a user and prints the details nicely"""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    first = input("Enter first name: ")
    last = input("Enter last name: ")
    email = input("Enter e-mail: ")

    while email:      #this is always true since email is not an empty string
        if catch_email(email):
            break
        else:
            print("wrong email enter again")
            email = input("")

    n = len(last)
    password = ""
    r_st = []

    for i in range(5):
        r_st.append(random.choice(alphabet))

    password = first[0:2] + last[-1:-3] + "".join(r_st)
    print(f"your password is {password}. do you like it ?(enter yes or no)")
    choice = input("")

    if choice == "yes":
        user = User(first,last,email,password)
        users.append(user)
        pprint.pprint(user)
    else:
        print("Enter your own password: ")
        password = input("")
        while password:    #this is always true since password is not an empty string
            if catch_password(password):
                password = password
                break
            else:
                print("password not up to or greater than 7 characters, enter again")
                password = input("")
        user = User(first,last,email,password)
        users.append(user)
        pprint.pprint(user)

register()