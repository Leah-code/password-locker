#!/usr/bin/env python3.6
from credetial import User, Credetial
import random
import getpass



def create_user(first_name,second_name,user_name,email,password):
    new_user = User(first_name,second_name,user_name,email,password)
    return new_user

def save_user(user):
    user.save_user()
    
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
    
def find_user_credetials(Accountname):
    return Credetial.find_by_Accountname(Accountname)

def check_existing_credetials(Accountname):
    return Credetial.credetials_exists(Accountname)

def display_Accountname():
    return Credetial.display_credetials()

# def display_user_credetials():
#     return Credetial.display.user_credetials()

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
                        if display_Accountname():
                            print('_' * 10)
                            for credetials in display_Accountname():
                                print(f'SEARCH RESULTS\n Accountname: {credetials.Accountname}\n Username: {credetials.loginname}\n  Password: {credetials.accountpasssword}\n ')
                            print('_' * 10)
                        else:
                            print("No such results..")
                            print("\n")
                elif short_code == 'look':
                            search = input("ENTER ACCOUNTNAME:.?")
                            if check_existing_credetials(search):
                                search_account = find_user_credetials(search)
                                print(f'Accountname: {search_account.Accountname}\n Username: {search_account.loginname}\n ..Password: {search_account.accountpassword}\n ')
                            else:
                                print('NONE_EXISTING ACCOUNT')
                elif short_code == 'quit':
                            print("WELCOME BACK AGAIN...(direct feedback@katana.com)")
                            break
                            
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        #   elif ac_code == 's':
                        #             sec = input('please enter the secret key of the account you want to search for: ')
                        #             if check_existing_credentials(sec):
                        #                 search_secret = find_credential(sec)
                        #                 print(f'account: {search_secret.account} \n account-password: {search_secret.ac_password}')
                        #             else:
                        #                 print('the account doesn\'t exist')
                        #         elif ac_code == 'ex':
                        #             print('exiting')
                        #             break

if __name__ == '__main__':
    main()