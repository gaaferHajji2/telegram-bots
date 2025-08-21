from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from dotenv import load_dotenv

import os

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await update.message.reply_text("Hello Telegram Bot by JLoka World") # type: ignore
        await update.message.reply_text(f'Hello {update.effective_user.first_name}') # type: ignore
    except Exception as e:
        print(f"The Error msg of start-command is: {e}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    try:
        user_txt = update.message.text.lower() # type: ignore

        if "hello" in  user_txt:
            await update.message.reply_text("Hi, How I can help You") # type: ignore
        else:
            await update.message.reply_text(f"Your text is: {user_txt}") # type: ignore
    except Exception as e:
        print(f"Error msg in echo-command, with msg: {e}")

def main():
    TOKEN = os.environ.get('TOKEN', 'NULL');

    print(f"Token is: {TOKEN}")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start));
    app.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND, echo))

    app.run_polling()

if __name__ == '__main__':
    main()