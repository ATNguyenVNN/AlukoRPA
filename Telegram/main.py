# pip install python-telegram-bot
from telegram.ext import *
import time, random
import keys
from mes import RPA_MES
print('Starting up bot...')

# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')

# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')

def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hey there! Welcom to AI System from ALUKOVN.'

    if 'how are you' in text:
        return 'I\'m good!'

    if '300000' in text:
        # Auto Create Purchase Order Subcontract.
        time.sleep(5)
        po_number = []
        for pr_number in list(text.split(",")):
            #print(pr_number)
            po_number.append(int(pr_number) + 1600000000)
            #print("--------")
        message = "Purchase Order Subcontract List:\n--------\n Created: {} \n--------\n Not Yet Created: XXX \n--------\n Message Automatic from AI_ALUKOVN.".format(",".join([str(char) for char in po_number]))
        return message
    if '810000' in text:
        # Auto GR to Main Warehouse
        time.sleep(5)
        data = []
        for tx in list(text.split(" ")):
            data.append(tx)
        print(data[1],data[0],data[2],str(data[3]).upper(),data[4])
        rpa = RPA_MES('http://10.12.40.3/', 'hav1', '1')
        rpa.mes_login()
        rpa.mes_tab('30930001')
        return rpa.mes_30930001(data[1],data[0],data[2],str(data[3]).upper(),data[4],)
        
    return 'I don\'t understand. Contact to Administrator...'

def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    #text = str(update.message.text).lower()
    text = str(update.message.text).lower().replace('\n' or ' ', ',').strip("/")
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.from_user.first_name}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@ai_aluko_bot' in text:
            new_text = text.replace('@ai_aluko_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)


    # Reply normal if the message is in private
    update.message.reply_text(response)

# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(keys.token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()