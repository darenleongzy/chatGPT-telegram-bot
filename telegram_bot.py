import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from chatGPT import create_query

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
count = 0
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE, count = 0):
    count +=1
    logging.info('User Number: '+ str(count) + ' - ' + update.effective_user.first_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello "+ update.effective_user.first_name + ", I have been waiting for you!")

async def end(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Great chat, talk to you soon!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=create_query(update.message.text))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('end', end))
    application.add_handler(echo_handler)

    application.run_polling()
