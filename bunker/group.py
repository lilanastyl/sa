import random
import string

groups = { }

class Group:
    def __init__(self, name):
        self.name = name
        self.code = self.generate_code()
        self.players = []

    def generate_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    def players_connect(self, message):
        self.players.append(message)