import unittest  #IMPORTING THE MODULE FOR TESTING....
from credetial import User  #IMPORTING THE CLASS...

 class TestCredetial(unittest.TestCase):
    def setUp(self):
         self.new_user =("hussein","katana","husseinkatana17@gmail.com","mzinge2019","password")
    def tearDown(self):
        User.user_list = []
    def test_unit():
        self.assertEqual(self.new_first_name,"hussein")
        self.assertEqual(self.new_last_name,"katana")
        self.assertEqual(self.new_email,"husseinkatana17@gmail.com")
        self.assertEqual(self.new_password,"mzinge2019")
        self.assertEqual(self.new_user,"password")
if __name__ == '__main__':
    unittest.main()    