#!/usr/bin/env python3.6
from credetial import User, Credetial
import random
import getpass



def create_user(first_name,second_name,user_name,email,password):
    new_user = User(first_name,second_name,user_name,email,password)
    return new_user

def save_user(user):
    user.save_credetials()
    
def del_user(user):
    user.delete_user()
    
def create_credetials(Accountname,loginname,accountpassword,secretkey):
    new_credetials = Credetial(Accountname,loginname,accountpassword,secretkey)
    return new_credetials

def save_users(user):
    user.save_users()
    
def delete_user_credetials(user):
    user.delete_user()
    
def confirm_user(email,password):
    confirm_user = User.valid_user(email,password)
    return confirm_user

def del_user(user):
    user.delete_user()
    
def find_credetials(Accountname):
    return Credetial.find_by_Accountname(Accountname)

def check_credetials(Accountname):
    return Credetial.credetials_exists(Accountname)

def display_Accountname(self):
    return Credetial.display_credetials(self)

#def display_credetials():
    #return Credetial.display_credetials()
    

def main():
            print("Welcome to passwordlocker.WHATS YOUR NAME?")
            user_name = input().upper()
            print(f"HELLO {user_name}.DO YOU WANT TO SAVE YOUR PASSWORDS")
            print("\n")
            while True:
                print("use this short code: save - saving a new contact, see - display your saved passwords,  look -  to find a password, quit -exit the option")
                short_code = input().lower()

                    # Account_name,login_name,acc_password,secret_key
                if short_code == 'save':
                        print("Account_name")
                        Accountname = input()
                        print("login_name")
                        loginname = input()
                        print ("accountpasssword")
                        accountpasssword = input()                        
                        save_user(Credetial(Accountname,loginname, accountpasssword))
                        print(f'here are your account details: .{Accountname}..{loginname}...{accountpasssword}')
                elif short_code == 'see':
                        if display_Accountname(Accountname):
                            print('_' * 10)
                            for credetials in display_Accountname():
                                print(f'SEARCH RESULTS\n Accountname: {credetials.Accountname}\n Username: {credetials.loginname}\n  Password: {credetials.accountpasssword}\n ')
                            print('_' * 10)
                        else:
                            print("No such results..")
                            print("\n")
                elif short_code == 'look':
                            search = input("ENTER ACCOUNTNAME:.?")
                            if check_credetials(search):
                                search_Accountname = find_credetials(search)
                                print(f'Accountname: {search_Accountname.Accountname}\n Username: {search_Accountname.loginname}\n ..Password: {search_Accountname.accountpassword}\n ')
                            else:
                                print('NONE_EXISTING ACCOUNT')
                elif short_code == 'quit':
                            print("WELCOME BACK AGAIN...(direct feedback@katana.com)")
                            break
                  

if __name__ == '__main__':
    main()