import random
import string
import pyperclip

class User:
    '''
    Class that generates instance of user details
    '''
#Test one

    users_list=[] #users will be saved here.

    def __init__(self, first_name, last_name, password):
        '''
        _init_method that help us define properties for our objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.password = password


    def save_user(self):
        '''
        save_user method that save user objects in the users_list
        '''
        User.users_list.append(self)


    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method checks if the name and the password entered match entries in the users list.
        '''
        current_user = ''
        for user in User.users_list:
            if(user.first_name == first_name and user.password == password):
                current_user = user.first_name
        return current_user


class Details:
    '''
    In this class the user maybe able to enter their other accounts details and save passwords and information.
    '''

    details_list = []
    users_details_list = []

    def __init__(self, user_name, website_name, account_name, password):
        '''
        _init_method us define our object's properties.
        '''

        self.user_name = user_name
        self.website_name = website_name
        self.account_name = account_name
        self.password = password


    def save_detail(self):
        '''
        This method save details in the details_list.
        '''

        Details.details_list.append(self)


    def generate_password(self):
        '''
        Function to generate a password where a user can create a password based on their length of choice.
        '''
        chars = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890^?!?$%&/()=?`'+#*'~';:_,.-<>|"
        password = ""

        length = int(input("[*] Input Password Length: "))
        while len(password) != length:
            password = password + random.choice(chars)
            if len(password) == length:
                print("Password: %s" % password)
        return password


    def del_detail(self):
        '''
        Method that deletes a saved detail from the detail_list
        '''
        Details.details_list.remove(self)


    @classmethod
    def display_detail(cls, user_name):
        '''
        Class method to show the list of details saved
        '''
        users_details_list = []
        for detail in cls.details_list:
            if detail.user_name == user_name:
                users_details_list.append(detail)
        return users_details_list


    @classmethod
    def find_my_website_name(cls, website_name):
        '''
        Class method that takes a website name and returns the details that matches that website.
        '''
        for detail in cls.details_list:
            if detail.website_name == website_name:
                return detail


    @classmethod
    def copy_detail(cls, website_name):
        '''
        Method copies credential details after user has entered their website_name.
        '''
        find_detail = Details.find_my_website_name(website_name)
        return pyperclip.copy(find_detail.password)


    @classmethod
    def detail_exist(cls, website_name):
        '''
        Class method that checks if a detail exists.
        '''
        for detail in cls.details_list:
            if detail.website_name == website_name:
                return True
        return False