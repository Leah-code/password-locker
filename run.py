#!/usr/bin/env python3.6

from credetial import User, Credetial, display_user_credetials
# import random
# import getpass



def create_user(first_name,second_name,user_name,email,password):
    new_user = User(first_name,second_name,user_name,email,password)
    return new_user
def save_user(user):
    user.save_user()
def del_user(user):
    user.delete_user()
def create_user_credetials(Accountname,loginname,mypassword,secretkey):
    new_user_credetials = Credetial(Accountname,loginname,mypassword,secretkey)
    return new_user_credetials
def save_user_credetiaals(user_credetials):
    user_credetials.save_user_credetils()
def delete_user_credetials(user_credetials):
    user_credetials.delete_user_credetials()
# def confirm_user(email,password)
#     confirm_user = User.valid_user(email,password)
#     return confirm_user
def del_user_credetials(user_credetials):
    user_credetials.delete_user_credetials()
def find_user_credetials(secretkey):
    return Credetial.find_by_secretkey(secretkey)
def check_existing_user_create_user_credetials(secretkey):
    return Credetial.user_credetials_exist(secretkey)
def display_secret_key():
    return Credetial.display_user_credetials
def display_user_credetials():
    return Credetial.display.user_credetials()

def main():
            print("Welcome to passwordlocker.WHATS YOUR NAME?")
            user_name = input().upper()
            print(f"HELLO {user_name}.DO YOU WANT TO SAVE YOUR PASSWORDS")
            print("/N")
            while True:
                print("use this short code: save - saving a new contact, see - display your saved passwords, dele - to delete your saved passwords, look -  to find a password, quit -exit the option")
                short_code = input().lower()

                    # Account_name,login_name,acc_password,secret_key
                if short_code == 'save':
                        print("Account_name")
                        Accountname = input()
                        print("login_name")
                        loginname = input()
                        print ("mypassword")
                        accountpassword = input()
                        print("secretkey")
                        secret_key = input()  
                        
                        save_user_credetiaals(Credetial(Accountname,loginname,mypassord,secretkey))
                        print(f'here are your account details: \n......{Accountname}\n........{loginname}\n..........{mypassword}.....{secretkey}')
                        # save_credetials(save_user_credetials(Account_name, login_name, acc_password, secret_key))
                    # print(f"new_user_credetials{Account_name} {login_name} {acc_password} {secret_key} created")
                # elif short_code == 'see':
                #         if display_user_credetials():
                #             print("HERE IS A LIST OF YOUR PASSWORDS FOR DIFFERENT ACCOUNT")
                #             print("/n")
                #             for credetials in display_user_credetials():
                #                 print(f"{user_credetials.Account_name} {user_credetials.login_name} {user_credetials.acc_password}  {user_credetials.secret_key}")
                #                 print("/n")
                # elif short_code == 'look':
                #         print("ENTER THE SECRET_KEY YOU WANT TO FIND")
                #         secret_key = input()
                #         if check_existing_user_credetials(secret_key):
                #             search_user_credetials = find_user_credetials(secret_key)
                #             print(f"{search_user_credetials.Account_name} {search_user_credetials.login_name}  {search_user_credetials.acc_password} {search_user_credetials.secret_key}")
                #             print('_' * 25)
                #             print(f"Account-name....{search_user_credetials.Account_name}")
                #             print(f"Login-name....{search_user_credetials.login_name}")
                #             print(f"Password....{search_user_credetials.acc_password}")
                #             print(f"Unique-key....{search_user_credetials.secret_key}")
                #         else:
                #             print("THAT ACCOUNT IS NOT RECOGONISED")
                # elif short_code == "quit":
                #     print("SEE YOU NEXT TIME DEAR FRIEND")
                # else:
                #     print("WRONG CHOICE....")
                
if __name__ == '__main__':
    main()