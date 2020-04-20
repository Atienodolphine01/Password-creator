import unittest
import user_details_test, user_details_test
from user_details import Details


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    
    
    def setUp(self):
        '''
        Set up method to run before each check if pyperclip is installedtest cases.
        '''
        self.new_user = user('Dolphine', 'Atieno', 'Dolphine0123')

    def test_init_(self):
        '''
        Test case to see if the object is initialised properly.
        '''
        self.assertEqual(self.new_user.first_name, 'Dolphine')
        self.assertEqual(self.new_user.last_name, 'Atieno')
        self.assertEqual(self.new_user.password, 'Dolphine0123')

    def tearDown(self):
        '''
        A method that clears the users list after every test.
        '''
        User.users_list = []


    def test_save_user(self):
        '''
        Test case to confirm if user object is saved to the users list.
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list),1)



