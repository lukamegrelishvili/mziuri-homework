class MailSender:
    def send_mail(self, email, message):
        print(f"Sending mail to {email}: {message}")


class Contacts:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Friend(Contacts, MailSender):
    def __init__(self, name, phone, email):
        super().__init__(name, phone)
        self.email = email

    def send_mail(self, message):
        super().send_mail(self.email, message)


class Family(Contacts, MailSender):
    def __init__(self, name, phone, email, birthdate):
        super().__init__(name, phone)
        self.email = email
        self.birthdate = birthdate

    def send_mail(self, message):
        super().send_mail(self.email, message)


friend = Friend("Alice", "123-456", "alice@example.com")
family_member = Family("Bob", "789-012", "bob@example.com", "02/11/2001")

friend.send_mail("Hello Alice!")
family_member.send_mail("Happy Birthday Bob!")
