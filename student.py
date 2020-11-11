class Student:
    def __init__(self, firstname, lastname, email, ids, birthday=None):
        if birthday is None:
            birthday = '1.3.2001'

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.ids = ids
        self.birthday = birthday
