from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from dotenv import load_dotenv

import os

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello Telegram Bot by JLoka World") # type: ignore
    await update.message.reply_text(f'Hello {update.effective_user.first_name}') # type: ignore

def main():
    TOKEN = os.environ.get('TOKEN', 'NULL');

    print(f"Token is: {TOKEN}")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start));

    app.run_polling()

if __name__ == '__main__':
    main()