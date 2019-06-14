import unittest
from credetial import User

class TestCredetial(unittest.TestCase):
    def setUp(self):
        self.new_user =("hussein","katana","hussein2001","husseinkatana17@gmail.com","mzinge2019","password")
    def tearDown(self):
        User.user_list = []
    def test_unit(self):
        self.assertEqual(self.new_user.first_name,"hussein")
        self.assertEqual(self.new_user.second_name,"katana")
        self.assertEqual(self.new_user.user,"hussein2001")
        self.assertEqual(self.new_user.email,"husseinkatana17@gmail.com")
        self.assertEqual(self.new_user.password,"mzinge2019")
        self.assertEqual(self.new_user,"password")
    
if __name__ == '__main__':
    unittest.main()
