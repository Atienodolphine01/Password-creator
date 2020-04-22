import unittest
import user_details_test, user_details_test
import pyperclip
from user_details import Details
from user_details import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    '''
    
    
    def setUp(self):
        '''
        Method to run before test cases.
        '''
        self.new_user = User("Dolphine", "Atieno", "dolphine0123")

    def test__init__(self):
        '''
        Test case to see if the object is initialised properly.
        '''
        self.assertEqual(self.new_user.first_name, "Dolphine")
        self.assertEqual(self.new_user.last_name, "Atieno")
        self.assertEqual(self.new_user.password, "dolphine0123")

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
        self.assertEqual(len(User.users_list), 1)



    def test_check_user(self):
        '''
        Test whether login feature is functioning.
        '''
        self.new_user = User('Dolphine', 'Atieno', 'dolphine0123')
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
        self.new_detail = Details("Dolphine", "Facebook", "dalphine", "atieno1997")

    def test__init__(self):
        '''
        Test case to check if details created is properly done.
        '''
        self.assertEqual(self.new_detail.user_name, "Dolphine")
        self.assertEqual(self.new_detail.website_name, "Facebook")
        self.assertEqual(self.new_detail.account_name, "dalphine")
        self.assertEqual(self.new_detail.password, "atieno1997")

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
        instagram = Details("Deyalasoul", "Instagram", "Deyala", "Roseflower01")
        instagram.save_detail()
        self.assertEqual(len(Details.details_list), 2)


    def test_display_details(self):
        '''
        Test case to test if objects show.
        '''
        self.new_detail.save_detail()
        instagram = Details("Deyalasoul", "Instagram", "Deyala", "Roseflower01")
        instagram.save_detail()
        twitter = Details('Bill', 'Twitter', 'billy', 'billyboss')
        twitter.save_detail()
        self.assertEqual(len(Details.display_detail(instagram.user_name)), 1)


    def test_find_my_website_name(self):
        '''
        Test case to test if we can search credential by site_name and return the correct credential.
        '''
        self.new_detail.save_detail()
        twitter = Details('Bill', 'Twitter', 'billy', 'billyboss')
        twitter.save_detail()
        detail_exist = Details.find_my_website_name('Twitter')
        self.assertEqual(detail_exist, twitter)


    def test_copy_details(self):
        '''
        Test casse to test if the copy detail function copies the correct detail of the user.
        '''
        self.new_detail.save_detail()
        facebook = Details('Dolphine', 'Facebook', 'dalphine', 'atieno1997')
        facebook.save_detail()
        find_detail = None
        for detail in Details.users_details_list:
            find_detail = Details.find_my_website_name(detail.website_name)
            pyperclip.copy(find_detail.password)
        Details.copy_detail(self.new_detail.website_name)
        self.assertEqual('atieno1997', pyperclip.paste())


    def test_delete_detail(self):
        '''
        Test to see if we can delete a saved detail
        '''
        self.new_detail.save_detail()
        new_detail = Details('Bill', 'Twitter', 'billy', 'billyboss')
        new_detail.save_detail()

        self.new_detail.del_detail()
        self.assertEqual(len(Details.details_list), 1)


    def test_credential_exists(self):
        '''
        Test case to confirm if a detail exist in the detail_list.
        '''
        self.new_detail.save_detail()
        test_detail = Details('Bill', 'Twitter', 'billy', 'billyboss')
        test_detail.save_detail()

        detail_exists = Details.detail_exist("Twitter")
        self.assertTrue(detail_exists)


if __name__ == '__main__':
    unittest.main()