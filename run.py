from user_details import Details, user

def create_user(fname, lname, password):
    '''
    Function creates a new user account.
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    Function saves a new user.
    '''
    User.save_user(user)


def verify_user(first_name,password):
    '''
    Function verify if user exist.
    '''
    checking_user = User.check_user(first_name, password)
    return checking_user


def generate_password(self):
    '''
    function enables user to generate password.
    '''
    gen_password = Details.generate_password(self)
    return gen_password


def create_detail(user_name, website_name, account_name, password):
    '''
    Function creates new user details.
    '''
    new_detail = Details(user_name, website_name, account_name, password)
    return new_detail


def display_details(username):
    '''
    Fucntion to display details saved.
    '''
    return Details.display_detail(username)
def copy_detail(website_name):
    '''
    Function that copies credentials details to the clipboard.
    '''
    return Details.copy_detail(website_name)


def find_my_website(website_name):
    '''
    Function that searches for a website name.
    '''
    return Details.find_my_website_name(website_name)

def delete_detail(detail):
    '''
    Function that deletes details by website name.
    '''
    detail.del_detail()

def check_existing_details(website_name):
    '''
    Function that checks if a detail exists.
    '''
    return Details.detail_exist(website_name)


def main():
    print('\n')

    print('')
    print("Hi! Welcome to Password Creator.")
    while True:
        print("*"*60)
        print('\n')
        print("Use this codes to navigate: \n ca - Create an account \n li - Log in \n ex - Exit")
        print('\n')
        short_code = input("Enter a choice: ").lower().strip()


        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print('\n')
            print("-"*60)
            print('\n')
            print("To create a new account:")
            first_name = input('Enter your first name - ').strip()
            last_name = input('Enter your last name - ').strip()
            password = input('Enter password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print('\n')
            print(f"New account created for {first_name} {last_name} using password {password}")


       elif short_code == 'li':
            print("-"*60)
            print('\n')
            print("Enter your account details to log in.")
            user_name = input("Enter your first name - ").strip()
            password = str(input("Enter your password - "))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print('\n')
                print(f"Welcome {user_name}. Please choose an option to continue.")
                while True:
                    print("-"*60)
                    print("Navigation codes: \n cc - To create a detail \n dc - To display all details \n fc - To find a detail \n cp - To copy password \n del - To delete a detail \n ex - Exit")
                    print('\n')
                    short_code = input('Enter your choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'ex':
                        print('\n')
                        print(f"Goodbye {user_name}")
                        break
                    elif short_code == 'cc':
                        print('\n')
                        print("Enter your credential details:")
                        website_name = input("Enter the website's name - ").strip()
                        account_name = input("Enter your account's username - ").strip()


                        while True:
                            print('\n')
                            print("-"*60)
                            print("Choose the password option you would like. Use keys: \n ep - To enter a password \n gp - To generate a password \n ex - Exit")
                            password_choice = input("Enter an option: ").lower().strip()
                            print("-"*60)
                            if password_choice == 'ep':
                                print('\n')
                                password = input("Enter your password: ").strip()
                                break
                                
