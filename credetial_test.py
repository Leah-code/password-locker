import unittest
from credetial import User
# self,first_name,second_name,user_name,email,password)
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("hussein","katana",'hussein2001',"husseinkatana17@gmail.com","mzinge2019")
    def tearDown(self):
        User.user_list = []
    def test_unit(self):
        self.assertEqual(self.new_user.first_name,"hussein")
        self.assertEqual(self.new_user.second_name,"katana")
        self.assertEqual(self.new_user.user_name,"hussein2001")
        self.assertEqual(self.new_user.email,"husseinkatana17@gmail.com")
        self.assertEqual(self.new_user.password,"mzinge2019")
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
if __name__ == '__main__':
    unittest.main()
