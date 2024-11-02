from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
import os

# Environment Variables
TELEGRAM_BOT_TOKEN = "7949409636:AAG3Z6x624KUSXEUv35XtEY6Z1fr17hOBsI"

# Telegram Bot Setup
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# Function to handle the start command and send back the user's info
def start(update: Update, context):
    # Get the current user's ID and username
    telegram_user_id = update.effective_user.id
    telegram_username = update.effective_user.username or ""

    # Send a message with the user's ID and username
    response = {
        "telegram_user_id": str(telegram_user_id),
        "telegram_username": telegram_username
    }
    update.message.reply_text(f"User info: {response}")

# Set up the updater and dispatcher
updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Handler for the /start command
dispatcher.add_handler(CommandHandler("start", start))

# Handler for any text message
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, start))

# Start polling to receive updates
updater.start_polling()
updater.idle()