import pyperclip

class User:
    #class to generate new instance of the user
    user_list = []
    credetial_list = []
    
    def __init__(self,first_name,second_name,user_name,email,password):
        self.first_name = first_name
        self.second_name = second_name
        self.user_name = user_name
        self.email = email
        self.password = password
    
    @classmethod
    def confirm_users(cls,locker_user,password):
        old_user = ""
        for user in User.user_list:
               if user.locker_user and user.password == password:
                 old_user = user.locker_user
        return old_user
    
        pass
    
    
    def save_user(self):
        User.user_list.append(self)
    
     
    
    
        
        
class Credetial:
    credetials_list = []
    def __init__(self,Accountname,loginname,mypassword,secretkey):
        #docstring for simplicity.....
        self.Accountname = Accountname
        self.loginname = loginname
        self.mypassword = mypassword
        self.secretkey = secretkey
    
    
    def save_user_credetials(self):
        Credetial.credetials_list.append(self)
        
    def delete_user_credetials(self):
        Credetial.credetials_list.remove(self)
        
        
@classmethod
def find_by_secretkey(cls,secretkey):
    for credetials in cls.secretkey  == secretkey:
        return credetials

@classmethod
def user_credetials_exists(cls,Accountname):
        for account in cls.credetials_list:
            if account.secretkey == secretkey:
                return True
            else:
                return False

@classmethod
def display_user_credetials(cls):
    return cls.credetials_list