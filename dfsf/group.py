import telebot
from telebot import types
from telebot.async_telebot import AsyncTeleBot
import random
import string

class Group:
    def __init__(self, name):
        self.name = name
        self.code = self.generate_code()
        self.watchers = []
        self.players = []
    
    def add_user(self, message):
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