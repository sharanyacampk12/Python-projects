from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text= 'hello, world')
updater = Updater(token = '5624495275:AAHUj-rn101vr1gUWmkBqtgLaTpjJ_Kx89E',use_context=True)
dispatcher = updater.dispatcher
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()
