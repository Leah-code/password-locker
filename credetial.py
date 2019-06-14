class User:
    #class to generate new instance of the user
    user_list = []
    #user_credetial_list = []
    
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
        user.user_list.append(self)
    
     
    
    
        
        
        
    
    
    
    
    
    
    
    
    
# class credetials:
#     """
#     class to create user credetials
#     """
