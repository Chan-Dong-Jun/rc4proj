# from typing import Final
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
# TOKEN: Final = '7949409636:AAG3Z6x624KUSXEUv35XtEY6Z1fr17hOBsI'
# BOT_USERNAME: Final = '@rc4bookingbot'

# # Commands
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('Hello! Thanks for chatting with me! I am a banana!')

# async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('I am a banana! Please type something so I can respond!')

# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('This is a custom command!')


# def handle_response(text: str) -> str:
#     processed: str = text.lower()

#     if 'hello' in processed:
#         return 'Hey there!'

#     if 'how are you' in processed:
#         return 'I am good!'

#     if 'i love python' in processed:
#         return 'Remember to subscribe!'

#     return 'I do not understand what you wrote...'

# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     message_type: str = update.message.chat.type
#     text: str = update.message.text

#     print(f'User {update.message.chat.id} in {message_type}: "{text}"')

#     if message_type == 'group':
#         if BOT_USERNAME in text:
#             new_text: str = text.replace(BOT_USERNAME, '').strip()
#             response: str = handle_response(new_text)
#         else:
#             return
#     else:
#         response: str = handle_response(text)

#     print('Bot:', response)
#     await update.message.reply_text(response)
    
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f'Update {update} caused error {context.error}')


# if __name__ == '__main__':
#     print('Starting bot...')
#     app = Application.builder().token(TOKEN).build()

#     # Commands
#     app.add_handler(CommandHandler('start', start_command))
#     app.add_handler(CommandHandler('help', help_command))
#     app.add_handler(CommandHandler('custom', custom_command))

#     # Messages
#     app.add_handler(MessageHandler(filters.TEXT, handle_message))

#     # Errors
#     app.add_error_handler(error)

#     # Polls the bot
#     print('Polling...')
#     app.run_polling(poll_interval=3)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from telegram import Bot
import os

# Environment Variables
TELEGRAM_BOT_TOKEN = "7949409636:AAG3Z6x624KUSXEUv35XtEY6Z1fr17hOBsI" #os.getenv("TELEGRAM_BOT_TOKEN")  # Injected into env

# FastAPI app setup
app = FastAPI()

# Telegram Bot Setup
bot = Bot(token=TELEGRAM_BOT_TOKEN)

# User model for FastAPI
class UserRequest(BaseModel):
    telegram_user_id: int

@app.post("/get_user_info")
async def get_user_info(user: UserRequest):
    try:
        # Get the chat information from Telegram using telegram_user_id
        telegram_user_id = user.telegram_user_id
        chat = bot.get_chat(telegram_user_id)
        
        if chat:
            # Extract the username if it exists; else default to an empty string
            telegram_username = chat.username if chat.username else ""
            return {
                "telegram_user_id": str(telegram_user_id),
                "telegram_username": telegram_username
            }
        else:
            raise HTTPException(status_code=404, detail="Telegram User ID not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Running the script with FastAPI and Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)