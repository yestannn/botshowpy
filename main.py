from googlesheets import *
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackContext
from telegram import Update

def message_handler(update: Update, context: CallbackContext):
    text = update.message.text

    update.message.reply_text(text =  google_sort(str(text)) )

def main():
    print('Start')
    updater = Updater(token='971804795:AAFaS_inqqrHRXZ_Mk3CBAemJ5E6v10dtiI', use_context=True)
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
    updater.start_polling()
    updater.idle()



if __name__ == "__main__":
    main()
