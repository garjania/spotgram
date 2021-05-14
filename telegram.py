import requests
import json


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def forward_to_channel(self, message_id, from_id, to_id):
        url = self.base + "forwardMessage?disable_notification=True&chat_id=@{}&from_chat_id=@{}&message_id={}".format(to_id, from_id, message_id)
        r = requests.get(url)
        return json.loads(r.content)

