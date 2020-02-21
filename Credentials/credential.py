import pyperclip


class User:

    user_list = []
    def __init__(self, first_name, last_name, phone_number, email):

       

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def save_user(self):
        User.user_list.append(self)

       
    def delete_user(self):
        
        User.user_list.remove(self)


class Credentials:

    credentials_list = []  

    def __init__(self, account, password, user_name):

        self.account = account
        self.password = password
        self.user_name = user_name

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
       

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_password(cls, password):
        
    @classmethod
    def credentials_exist(cls, password):
        
        for credentials in cls.credentials_list:
            if credentials.password == password:
                return True

        return False

    
    @classmethod
    def display_all_credentials(cls):
        
        return cls.credentials_list