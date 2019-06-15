class User:
    #class to generate new instance of the user
    user_list = []
    # user_credetial_list = []
    
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
    user_credetials_list = []
    def __init__(self,Account_name,login_name,acc_password,secret_key):
        #docstring for simplicity.....
        self.Account_name = Account_name
        self.login_name = login_name
        self.acc_password = acc_password
        self.secret_key = secret_key
    
    
    def save_credetial(self):
        Credetial.user_credetials_list.append()
        
    def delete_credetials(self):
        Credetial.user_credetials_list.remove(self)
        
        
@classmethod
def find_by_secret_key(cls,secret_key):
    for credetials in cls.seccret_key  == secret_key:
        return credetials

@classmethod
def user_credetials_exists(cls,Account_name):
        for user_credetials in cls.user_credetials_list:
            if user_credetials.Account_name == Account_name:
                return True
            
            else:
                return False

@classmethod
def display_user_credetials(cls):
    return cls.user_credetials_list