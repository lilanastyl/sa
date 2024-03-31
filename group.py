from telebot.types import User, Message
from person import Person
from bunker import Bunker

class Group():
    def __init__(self):
        self.game_status = False
        self.players: list[Person] = []
        self.bunker = Bunker()
        self.message_taboo = False
    
    def choose_reset(self):
        for player in self.players:
            player.choose = False
    
    def votes_reset(self):
        for player in self.players:
            player.votes = 0
    
    def add_user(self, new_user: User):
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
    
    def get_user(self, id):
        for user in self.players:
            if int(id) == user.user_info.id:
                return user
        return False

    def delete(self, id):
        for user in self.players:
            if user.user_info.id == id:
                self.players.remove(user)
                return user

groups: dict[int, Group] = {}