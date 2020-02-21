import unittest 
from credentials import User, Credentials  
import pyperclip


class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Celine", "mmbone", "0719476296",
                             "celinekerrine@gmail.com") 

    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Celine")
        self.assertEqual(self.new_user.last_name, "mmbone")
        self.assertEqual(self.new_user.phone_number, "0719476297")
        self.assertEqual(self.new_user.email, "celinekerrine@gmail.com")

    def test_save_user(self):
       
        self.new_user.save_user()
    
        self.assertEqual(len(User.user_list), 1)

    def tearDown(self):
       
        Credentials.user_list = []

    def test_delete_user(self):
        
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials(
            "twitter", "celinemmbone3", "CelineMmbone")

    def test_init(self):
        self.assertEqual(self.new_credentials.account, "twitter")
        self.assertEqual(self.new_credentials.password, "celinemmbone3")
        self.assertEqual(self.new_credentials.user_name, "CelineMmbone")

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
       
        self.assertEqual(len(Credentials.credentials_list), 1)


    def tearDown(self):
        Credentials.credentials_list = []

    def test_delete_credentials(self):
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "twitter", "celinemmbone3", "CelineMmbone")  
        test_credentials.save_credentials()

    def test_find_credentials_by_password(self):
       

        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "twitter", "celinemmbone3", "CelineMmbone")  
        test_credentials.save_credentials()


    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credentials.
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "twitter", "celinemmbone3", "CelineMmbone") 
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exist("celinemmbone3")

        self.assertTrue(credentials_exists)

    def test_display_all_credentials(self):
        

        self.assertEqual(Credentials.display_all_credentials(),Credentials.credentials_list)
    
    def test_display_credentials(self):
        

        self.assertEqual(Credentials.display_all_credentials(),Credentials.credentials_list)
if __name__ == '__main__':
    unittest.main()  