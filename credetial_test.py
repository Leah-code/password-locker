import unittest
from credetial import User,Credetial
# self,first_name,second_name,user_name,email,password)
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("hussein","katana",'hussein2001',"husseinkatana17@gmail.com","mzinge2019")
    def tearDown(self):
        User.user_list = []
    def test_init(self):
        self.assertEqual(self.new_user.first_name,"hussein")
        self.assertEqual(self.new_user.second_name,"katana")
        self.assertEqual(self.new_user.user_name,"hussein2001")
        self.assertEqual(self.new_user.email,"husseinkatana17@gmail.com")
        self.assertEqual(self.new_user.password,"mzinge2019")
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        
    def test_save_multiple_users(self):
         self.new_user.save_user()
         test_user = User("Test","user","test@gmail.com","tested","pass")
         test_user.save_user()
         self.assertEqual(len(User.user_list),2)
    # def tearDown(self):
    #     User.user_list = []
        
        
    class TestCredetial(unittest.TestCase):
        # self,Account_name,login_name,acc_password,secret_key
        def setUp(self):
            self.new_credetials = Credetial("facebook","kadweka","mzinge300","12345")
        def test__init__(self):
            self.assertEqual(self.new_credetial.Account_name,"facebook")
            self.assertEqual(self.new_credetial.login_name,"kadweka")
            self.assertEqual(self.new_credetial.acc_password,"mzinge300")
            self.assertEqual(self.new_credetial.secret_key,"12345")
            #saving user credetials....
        def test_save_credetials():
            self.new_credetials.save_credetials()
            self.assertEqual(len(Credetial.user_credetial_list),1)
            #saving multiple user......
        def test_save_multiple_users_credetials(self):
            self.new_credetials.save_credetials()
            test_user_credetials = Credetial("instagrgm","mzinge11","mzinge8888","57753838")
            test_user_credetials.save_credetial()
            self.asserEqual(len(Credetial.user_credetial_list),2)
        def test_delete_credetials(self):
            self.new_credetials.save_user_credetials()
            test_user_credetials = Credetial("snapchat","hussein95","hakakaka","679277")
            test_user_credetials.save_credetial()
            self.new_credetials.delete_credetials()
            self.assertEqual(len(Credetial.user_credetial_list),2)
            
            
if __name__ == '__main__':
    unittest.main()
