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
        # self,Account_name,acc_password,secret_key
        def setUp(self):
            self.new_credetial = Credetial("facebook","kadweka","mzinge300","12345")
        def test__init__(self):
            self.assertEqual(self.new_credetial.Account_name,"facebook")
            self.assertEqual(self.new_credetial.login_name,"kadweka")
            self.assertEqual(self.new_credetial.acc_password,"mzinge300")
            self.assertEqual(self.new_credetial.secret_key,"12345")
        
if __name__ == '__main__':
    unittest.main()
