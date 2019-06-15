#!/usr/bin/env python3.6

from  credetial import User,Credetial



def create_user(first_name,second_name,user_name,email,password):
    new_user = User(first_name,second_name,user_name,email,password)
    return new_user
def save_user(user):
    user.save_user()
def del_user(user):
    user.delete_user()
def create_user_credetials(Account_name,login_name,acc_password,secret_key):
    new_user_credetials = Credetial(Account_name,login_name,acc_password,secret_key)
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
def find_user_credetials(secret_key):
    return Credetial.find_by_secret_key(secret_key)
def check_existing_user_create_user_credetials(secret_key):
    return Credetial.user_credetials_exist(secret_key)
def display_secret_key():
    return Credetial.display_user_credetials
def display_user_account():
    return Credetial.display.user_credetials()

# def main()

