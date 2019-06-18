import pyperclip
class User:

    #class to generate new instance of the users
    user_list = []
def __init__(self,username,email,password):
    self.username = username
    self.email = email
    self.password = password
def save_user(self):
    User.user_list.append(self)
def delete_user(self):
   User.user_list.remove(self)
def display_user(self):
    User.user_list

    @classmethod
    def display_user(cls):
        return cls.user_list

class Credetial:

    credetials_list = []
    def __init__(self,Accountname,loginname,accountpassword):
        #docstring for simplicity.....
        self.Accountname = Accountname
        self.loginname = loginname
        self.accountpassword = accountpassword
    def save_credetials(self):
        Credetial.credetials_list.append(self)
    def delete_credetials(self):
        Credetial.credetials_list.remove(self)
    def delete_credetials(self):
        Credetial.credetials_list.delete(self)
    @classmethod
    def find_by_Accountname(cls,Accountname):
        for credetials in cls.credetials_list:
            if credetials.Accountname == Accountname:
                return credetials
    @classmethod
    def credetials_exists(cls,Accountname):
            for credetials in cls.credetials_list:
                if Credetial.credetials_exists == Accountname:
                    return True
                else:
                    return False
    @classmethod
    def display_credetials(cls):
        return cls.credetials_list
