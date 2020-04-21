from user_details import Details, user

def create_user(fname, lname, password):
    '''
    Function creates a new user account.
    '''
    new_user = User(fname, lname, password)
    return new_user


