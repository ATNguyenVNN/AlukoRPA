import imp
import telegram as tl
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import requests as rq
from datetime import datetime
class Tele_ALK():
    def __init__(self):
        # 5616553456:AAFqN4s3s6Bhyh6xjeGfTCOkwFhedoU2ey0
        self.my_token = "5616553456:AAFqN4s3s6Bhyh6xjeGfTCOkwFhedoU2ey0"
        # Create BOT Telegram
        self.bot = tl.Bot(token = self.my_token)
        #bot.sendMessage(chat_id = "-846172455", text = "Sent from VSCode")
    def main():
        pass
    def responses(input_text):
        user_message = str(input_text).lower()
        if user_message in ("hello","hi", "sup",):
            return "Hey, How's it going?"
        return "I don't understand you"
        
    def send_test_message(self,group_id):
        try:
            random_number = random.randint(81000000, 81999999)
            message = "`Inbound Delivery Number {} Created.`\n \n Message Automatic from Aluko AI.".format(random_number)
        
            tele.bot.send_message(chat_id=group_id, text=message,
                                    parse_mode='Markdown')
            tele.bot.reply_to_message()

        except Exception as ex:
            print(ex)
    def get_lasted_message(self):
        resp = rq.get("https://api.telegram.org/bot5616553456:AAFqN4s3s6Bhyh6xjeGfTCOkwFhedoU2ey0/getUpdates?offset=-1")
        return resp.text

if __name__ == "__main__":
    tele = Tele_ALK()
    #print(tele.get_lasted_message())
    tele.send_test_message("-846172455")
    