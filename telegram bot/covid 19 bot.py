import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
updater = Updater(token = '5624495275:AAHUj-rn101vr1gUWmkBqtgLaTpjJ_Kx89E',use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()
def death_rate(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if(response.status_code==200):
        data = response.json()
        date = data['Date'][:10]
        ans = f"Covid 19 summary (as of {date}): \n";
        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                ans += 'Total ' + attribute[5::].lower() + ":" + str(value) + "\n" 
        print(ans)
        context.bot.send_message(chat_id=update.effective_chat.id, text=ans)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error, something went wrong.")

corona_summary_handler = CommandHandler('summary', death_rate)
dispatcher.add_handler(corona_summary_handler)
