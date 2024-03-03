import random
import string
from telebot import types

groups = { }

class Group:
    def __init__(self, name):
        self.name = name
        self.code = self.generate_code()
        self.watchers: list[types.Message] = []
        self.players: list[types.Message] = []

    def generate_code(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    def players_connect(self, message: types.Message):
        self.players.append(message)
    def watchers_connect(self, id):
        for message in self.players:
            if message.id == id:
                self.players.remove(message)
                self.watchers.append(message)
    def delete(self, id):
        for message in self.players:
            if message.id == id:
                self.players.remove(message)
        for message in self.watchers:
            if message.id == id:
                self.watchers.remove(message)
            
