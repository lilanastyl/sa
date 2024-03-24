from telebot.types import User, Message
from person import Person
from bunker import Bunker

class Game():
    def __init__(self):
        self.game_status = False
        self.players: list[Person] = []
        self.bunker = Bunker()
    
    def add_user(self, new_user: User):
        for user in self.players:
            if user.user_info.id == new_user.id:
                return True
        self.players.append(Person(new_user))

    def get_users(self):
        users_text = ""
        for user in self.players:
            if user.choose:
                users_text += '✅'
            else:
                users_text += '❌'
            users_text += f"  @{user.user_info.username}\n"
        return users_text
    
    def check_ready(self):
        for user in self.players:
            if not user.choose:
                return False
        return True
    
    def check_user(self, searched_user: User):
        for user in self.players:
            if searched_user.id == user.user_info.id:
                return user
        return False

    def delete(self, user_new: User):
        for user in self.players:
            if user.user_info.id == user_new.id:
                self.players.remove(user)

games: dict[int, Game] = {}