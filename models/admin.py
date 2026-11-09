from models.user import User

class Admin(User):
    def __init__(self, user_id, name, email, password, role):
        super().__init__(user_id, name, email, password)
        self.role = role

    def show_info(self):
        print("-----Admin Information-----")
        print(f"ID: {self.user_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Role: {self.role}")