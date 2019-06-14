class User:
    #class to generate new instance of the user
    user_list = []
    #user_credetial_list = []
    
    @classmethod
    def confirm_users(cls,locker_user,password):
        
        old_user = ""
        for user in user.user_list:
           if user.locker_user and user.password == password:
           old_user = user.locker_user
        return old_user
    def _init_(self,Account_name,email,password):
        self.Account_name = Account_name
        self.email = email
        self.password = password
    
    def save(parameter_list):
        pass
     
    
    
        
        
        
    
    
    
    
    
    
    
    
    
# class credetials:
#     """
#     class to create user credetials
#     """