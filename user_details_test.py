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



    def test_check_user(self):
        '''
        Test whether login feature is functioning.
        '''
        self.new_user = User('Dolphine', 'Atieno', 'Dolphine0123')
        self.new_user.save_user()
        user2 = User('Israel', 'Hawi', '@israel01')
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, User.check_user(user2,password, user2.first_name))

class TestDetails(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    def setUp(self):
        '''
        set up method to run before each test cases.
        '''
        self.new_detail = Details('Dolphine', 'Facebook', 'dalphine', 'atieno1997')

    def test_init_(self):
        '''
        Test case to check if details created is properly done.
        '''
        self.assertEqual(self.new_detail.user_name, 'Dolphine')
        self.assertEqual(self.new_detail.website_name, 'Facebook')
        self.assertEqual(self.new_detail.account_name, 'dalphine')
        self.assertEqual(self.new_detail.password, 'atieno1997')

    def tearDown(self):
        '''
        This method clears users details after every test.
        '''
        Details.details_list = []


    def test_save_details(self):
        '''
        Test case to check if we can save details to the details list.
        '''
        self.new_detail.save_detail()
        instagram = Details('Deyalasoul', 'Instagram', 'Deyala', 'Roseflower01')
        instagram.save_detail()
        self.assertEqual(len(Details.details_list), 2)


    def test_display_details(self):
        '''
        Test case to test if objects show.
        '''
        self.new_detail.save_detail()
        instagram = Details('Deyalasoul', 'Instagram', 'Deyala', 'Roseflower01')
        instagram.save_detail()
        twitter = Details('Bill', 'Twitter', 'billy', 'billyboss')
        twitter.save_detail()
        self.assertEqual(len(Details.display_detail(instagram.user_name)), 1)

