import random
import string

class Generators:

    def generate_email(self, length):
        characters = string.ascii_lowercase + string.digits
        email = ''.join(random.choice(characters) for i in range(length)) + "@example"
        return email

    def generate_password(self, length):
        characters = string.ascii_lowercase + string.digits
        password = ''.join(random.choice(characters) for i in range(length))
        return password
