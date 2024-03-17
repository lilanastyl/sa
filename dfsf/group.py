from telebot.types import User, Message

class Game():
    def __init__(self):
        self.game_status = False
        self.players: list[list[User, bool]] = []
        # self.start_message_id = None
        # self.chat_group_id = None
    
    def add_user(self, new_user: User):
        for user in self.players:
            if user[0].id == new_user.id:
                return True
        self.players.append([new_user, False])

    def get_users(self):
        users_text = ""
        for user in self.players:
            if user[1]:
                users_text += '✅'
            else:
                users_text += '❌'
            users_text += f"  @{user[0].username}\n"
        return users_text
    
    def check_ready(self):
        for user in self.players:
            if not user[1]:
                return False
        return True

    def delete(self, user_new: User):
        for user in self.players:
            if user[0].id == user_new.id:
                self.players.remove(user)

games: dict[int, Game] = {}