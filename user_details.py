class user:
    '''
    Class that generates instance of user details
    '''
#Test one

    users_list=[] #users will be saved here.

    def _init_(self, first_name, last_name, password):
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