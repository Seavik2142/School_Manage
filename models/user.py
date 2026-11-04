from abc import ABC, abstractmethod

class User(ABC):
    total_users = 0

    def __init__(self , user_id , name , email , password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.__password = password
        User.total_users += 1


    def verify_password(self, password):
        return self.__password == password


    @abstractmethod
    def show_info(self):
        pass

    @classmethod
    def show_total_users(cls):
        print(f"Total users: {cls.total_users}")

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    def __str__(self):
        return f"{self.user_id} - {self.name} "

    