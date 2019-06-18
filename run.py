#!/usr/bin/env python3.6
from credetial import User, Credetial
import random
import getpass



def create_user(username,email,password):
    create_user = User(username,email,password)
    return create_user

def save_user(user):
    User.save_user()

def del_user(user):
    user.delete_user()

def create_credetials(Accountname,loginname,accountpassword,secretkey):
    create_credetials = Credetial(Accountname,loginname,accountpassword,secretkey)
    return create_credetials

def save_credetials(user):
    user.save_credetials()

def delete_credetials(user):
    user.delete_credetials()

# def confirm_user(email,password):
#     confirm_user = User.valid_user(email,password)
#     return confirm_user
#
# def del_user(user):
#     user.delete_user()

def find_credetials(Accountname):
    return Credetial.find_by_Accountname(Accountname)

def check_credetials(Accountname):
    return Credetial.credetials_exists(Accountname)

def display_Accountname():
    return Credetial.display_credetials()


def main():
            print("WHATS YOUR NAME?")
            user_name = input().upper()
            print(f"HELLO {user_name}.WELCOME TO BEST PASSWORDLOCKER\n select what you would want to do.")
            print("\n")
            while True:
                print(":\nmake-create a user account\nsave - saving a new contact\nsee - display your saved passwords\nlook -  to find a password\nquit -exit to exit credetial")
                short_code = input().lower()
                    # Account_name,login_name,acc_password,secret_==key
                if short_code == 'make':
                        print('USER-NAME')
                        username = input()
                        print('EMAIL')
                        email = input()
                        print('PASSWORD')
                        password = input()
                        username(create_user(username,email,password))
                        print(f'PRO-DETAILS:\nPro-user:{username}\nEmail:{email}\nPassword:{password}')
                elif short_code == 'save':
                        print("Account_name")
                        Accountname = input()
                        print("login_name")
                        loginname = input()
                        print ("accountpasssword")
                        accountpasssword = input()
                        save_credetials(Credetial(Accountname,loginname, accountpasssword))
                        print(f'DETAILS FOR YOUR :\n{Accountname}\n{loginname}\n{accountpasssword}')
                elif short_code == 'see':
                        if display_Accountname():
                            print('_' * 10)
                            for credetials in display_Accountname():
                                print(f'SAVED ACCOUNTS\nACCOUNT-NAME:{credetials.Accountname}\nUSER-NAME:{credetials.loginname}\nPASSWORD:{credetials.accountpassword}\n')
                            print('_' * 10)
                elif short_code == 'look':
                            search = input("ENTER ACCOUNTNAME?")
                            if check_credetials(search):
                                search_Accountname = find_credetials(search)
                                print(f'Accountname: {search_Accountname.Accountname}\n Username: {search_Accountname.loginname}\n ..Password: {search_Accountname.accountpassword}\n ')
                elif short_code == 'quit':
                            print("WELCOME BACK AGAIN...(direct feedback@katana.com)")
                            break
                elif short_code !="quit/look/see/make/save":
                            print(f"SORRY {user_name} YOU SELECTED THE WRONG CHOICE..")
                            break




if __name__ == '__main__':
    main()
