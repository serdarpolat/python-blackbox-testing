import student as st


class TestStudentClass:
    # VALID VALUE
    valid_std = st.Student('John', 'Doe', 'johndoe@email.com', '1234567')

    # INVALID VALUES
    # First letter of firstname is not capital
    invalid_std_1 = st.Student('john', 'Doe', 'john.doe@email.com', '1234567')
    # First letter of lastname is not capital
    invalid_std_2 = st.Student('John', 'doe', 'john.doe@email.com', '1234567')
    # Email has number char(s)
    invalid_std_3 = st.Student('John', 'Doe', 'john.doe1@email.com', '1234567')
    # Id has a alphabet char(s)
    invalid_std_4 = st.Student('John', 'Doe', 'john.doe@email.com', '1234567a')
    # Id has tow same number chars side by side
    invalid_std_5 = st.Student('John', 'Doe', 'john.doe@email.com', '12334567')

    def check_firstname(self):
        check = next((True for i in range(1, len(self.valid_std.firstname))
                      if self.valid_std.firstname[i] == self.valid_std.firstname[i].capitalize()), False)
        if not self.valid_std.firstname.isalpha():
            raise ValueError(
                '(FIRSTNAME VALUE ERROR): You can not fill any number characters')
        elif check:
            raise ValueError(
                '(FIRSTNAME VALUE ERROR): Only first letter must be capital')
        elif self.valid_std.firstname.isalpha() and self.valid_std.firstname == self.valid_std.firstname.capitalize():
            return self.valid_std.firstname
        else:
            raise ValueError(
                '(FIRSTNAME VALUE ERROR): First character of firstname must be capital.')

    def check_lastname(self):
        check = next((True for i in range(1, len(self.valid_std.lastname))
                      if self.valid_std.lastname[i] == self.valid_std.lastname[i].capitalize()), False)
        if not self.valid_std.lastname.isalpha():
            raise ValueError(
                '(LASTNAME VALUE ERROR): You can not fill any number characters')
        elif check:
            raise ValueError(
                '(LASTNAME VALUE ERROR): Only first letter must be capital')
        elif self.valid_std.lastname.isalpha() and self.valid_std.lastname == self.valid_std.lastname.capitalize():
            return self.valid_std.lastname
        else:
            raise ValueError(
                '(LASTNAME VALUE ERROR): First character of lastname must be capital.')

    def check_email(self):
        check = next((True for item in self.valid_std.email.split(
            '@')[0] if item.isdigit()), False)

        if not check:
            return self.valid_std.email
        else:
            raise ValueError(
                '(EMAIL VALUE ERROR): Each email\'s characters must be alphabetical')

    def check_id(self):
        check = True
        error = ''

        for i in self.valid_std.ids:
            if not i.isdigit():
                check = False
                error += 'Each characters of id must be number.'
                break

        for i in range(1, len(self.valid_std.ids)):
            if self.valid_std.ids[i] == self.valid_std.ids[i-1]:
                check = False
                error += ' Do not fill the same numbers side by side.'
                break

        if check:
            return self.valid_std.ids
        else:
            raise ValueError('(ID VALUE ERROR): {}'.format(error))

    def check_birthday(self):
        day = int(self.valid_std.birthday.split('.')[0])
        month = int(self.valid_std.birthday.split('.')[1])
        year = int(self.valid_std.birthday.split('.')[2])

        if day in range(1, 32) and month in range(1, 13) and 1920 <= year <= 2020:
            return self.valid_std.birthday
        else:
            raise ValueError(
                '(BIRTHDAY ERROR):Check your birthday. It seems you filled it wrong.')
