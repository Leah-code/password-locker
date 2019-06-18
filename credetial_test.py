import pyperclip
import unittest #for the unittest module
from credetial import User,Credetial

# self,first_name,second_name,user_name,email,password)
class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("hussein","mzinge2019")

    def test_init(self):
        self.assertEqual(self.new_user.username,"hussein")
        self.assertEqual(self.new_user.password,"mzinge2019")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),3)

    def test_save_multiple_users(self):
         self.new_user.save_user()
         test_user = User("tuch","nice")
         test_user.save_user()
         self.assertEqual(len(User.user_list),2)

    # def tearDown(self):
    #     User.user_list = []







    class TestCredetial(unittest.TestCase):
        # self,Accountname,loginname,accountpassword
        def setUp(self):
            self.new_credetials = Credetial("facebook","kadweka","mzinge300")

        def test__init(self):
            self.assertEqual(self.new_credetials.Accountname,"facebook")
            self.assertEqual(self.new_credetials.loginname,"kadweka")
            self.assertEqual(self.new_credetials.accountpassword,"mzinge300")


        def test_save_credetials(self):
            self.new_credetials.save_credetials() #saving new credetials
            self.assertEqual(len(Credetial.credetials_list),1)


        def test_save_multiple_credetials(self):
            self.new_credetials.save_credetials()
            test_credetials = Credetial("instagrgm","mzinge11","mzinge8888")
            test_credetials.save_credetials()
            self.asserEqual(len(Credetial.credetials_list),2)

        def test_delete_credetials(self):
            self.new_credetials.save_credetials()
            test_credetials = Credetial("snapchat","hussein95","hakakaka")
            test_credetials.save_credetials()
            self.new_credetials.delete_credetials()
            self.assertEqual(len(Credetial.credetials_list),1)

        def test_find_credetials_by_Accountname(self):
            self.new_credetials.save_credetials()
            test.credetials = Credetial("whatsapp","python88","muzinge210")
            test.credetials.save_credetials()
            found_credetials = Credetial.find_by_Accountname("Accountname")
            self.assertEqual(found_credetials.Accountname,test.credetials.Accountname)

        def test_credetials_exists(self):
            self.new_credetials.save_credetials()
            test_credetials = Credetial("twitter","kadweka77","hussein8149")
            test_credetials.save_credetials()
            credetials_exists = Credetial.credetials_exists("Accountname")
            self.assertTrue(test_credetials_exists)

        def test_disply_all_credetials(self):
            self.assertEqual(Credetial.display_credetials(),Credetial.credetials_list)




if __name__ == '__main__':
    unittest.main()
