# pip install python-telegram-bot
from tkinter import N
from telegram.ext import *
import time
import keys
import os
from func_selenium import RPA_MES


print('Starting up bot...')
group_b_id = 5439845726

# Lets us use the /start command


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')

# Lets us use the /help command


def help_command(update, context):
    update.message.reply_text(
        'Try typing anything and I will do my best to respond!')

# Lets us use the /custom command


def custom_command(update, context):
    update.message.reply_text(
        'This is a custom command, you can add whatever text you want here.')


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
            # print(pr_number)
            po_number.append(int(pr_number) + 1600000000)
            # print("--------")
        message = "Purchase Order Subcontract List:\n--------\n Created: {} \n--------\n Not Yet Created: XXX \n--------\n Message Automatic from AI_ALUKOVN.".format(",".join([
                                                                                                                                                                      str(char) for char in po_number]))
        return message
    # Auto GR to Main Warehouse
    if '810000' in text:
        time.sleep(1)
        data = []
        list_msg = []
        for line in list(text.split(",")):
            data.append(line)
        print(data)
        plant = ""
        for line in data:
            dt = line.split(" ")
            print("Bắt đầu xử lý: ", time.asctime( time.localtime(time.time()) ))
            print('Xử lý dữ liệu: ', dt[0], dt[1],
                  dt[2], dt[3], str(dt[4]).upper(), dt[5])
            if plant != dt[0]:
                # Xác định Plant.
                if dt[0] == '2120':
                    mes_usr = 'alk106470_tn'
                elif dt[0] == '2100':
                    mes_usr = 'alk106470_hy'
                elif dt[0] == '2300':
                    mes_usr = 'alk106470_alk'
                rpa = RPA_MES(keys.mes_ip, mes_usr, '1')
                # Tiến hành đăng nhập hệ thống.
                rpa.mes_login()
                plant = dt[0]
            msg = rpa.mes_30920001(dt[1],dt[2],dt[5])
            if msg[1] =='Hoàn tất kiểm tra số lượng mua...':
                if msg[0] == True:
                    msg = ' Không phải NVL giao về kho'
                    rpa.mes_tab('30930002')
                    msg = rpa.mes_30930002(dt[1],dt[2], dt[3])
                    list_msg.append(msg)
                else:
                    msg = 'Là NVL giao về kho VT'
                    rpa.mes_tab('30930001')
                    msg = rpa.mes_30930001(dt[1],dt[2], dt[3], str(dt[4]).upper(), dt[5])
                    list_msg.append(msg)
            else:
                msg = msg[1]
                list_msg.append(msg)
        return '\n'.join(list_msg)
    return 'Không hiểu đâuuu =).'


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower().replace(
        '\n' or ' ', ',').strip("/")
    response = ''

    # Print a log for debugging
    print(
        f'User {str(update.message.from_user.first_name) + " " + str(update.message.from_user.last_name)} says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@ai_aluko_bot' in text:
            new_text = text.replace(
                '@ai_aluko_bot', '').strip().replace("  ", ' ').strip()
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
    # Get Chat ID

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
