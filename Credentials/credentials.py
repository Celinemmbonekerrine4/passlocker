import pyperclip


class User:

    user_list = []
    def __init__(self, first_name, last_name, phone_number, email):

        # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_user(self):
        User.user_list.append(self)

        '''
        save_user method saves user objects into user_list
        '''

        def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    def delete_user(self):
        '''
        delete_user method deletes a saved credentials from the credentials_list
        '''

        User.user_list.remove(self)


class Credentials:

    credentials_list = []  # Empty password list
    # Init method up here

    # def save_credentials(self):
    #     pass

    def __init__(self, account, password, user_name):

        # docstring removed for simplicity

        self.account = account
        self.password = password
        self.user_name = user_name

        # save_password method saves password objects into password_list

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_password(cls, password):
        '''
        Method that takes in a password and returns a credential that matches that password.
        Args:
            password: password to search for
        Returns :
            Credentials of person that matches the password.
        '''

        # for password in cls.credentials_list:
        #     if credentials.password == password:
        #         return password
    @classmethod
    def credentials_exist(cls, password):
        '''
        Method that checks if a credentials exists from the contact list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                return True

        return False

    # @classmethod
    # def copy_email(cls,email):
    #     credentials_found = Credentials.find_by_email(email)
    #     pyperclip.copy(credentials_found.email)

    @classmethod
    def display_all_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list
