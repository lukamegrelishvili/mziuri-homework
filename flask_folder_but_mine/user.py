class User:
    ID = 0
    def __init__(self, fullname, email, password):
        self.fullname = fullname
        self.email = email
        self.password = password
        self.ID += 1

    def __str__(self):
        return f"full name: {self.fullname} email: {self.email} password: {self.password} ID: {self.ID}"
     