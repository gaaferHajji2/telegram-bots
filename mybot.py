import asyncio

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from dotenv import load_dotenv

import os

load_dotenv()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        await update.message.reply_text("Hello Telegram Bot by JLoka World") # type: ignore
        context.user_data["count"] = 0 # type: ignore
        context.user_data["step"] = "name" # type: ignore
        context.user_data["name"] = update.effective_user.first_name # type: ignore
        await update.message.reply_text(f'Hello {update.effective_user.first_name}') # type: ignore
    except Exception as e:
        print(f"The Error msg of start-command is: {e}")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    try:
        user_txt = update.message.text.lower() # type: ignore
        if context.user_data.get("count", ""): # type: ignore
            context.user_data["count"] +=1 # type: ignore
        else:
            context.user_data["count"] = 1 # type: ignore
        msg = f"This is Your {context.user_data['count']} to me" # type: ignore

        if "hello" in  user_txt:
            await update.message.reply_text(f"Hi, How I can help You, {msg}") # type: ignore
        elif "my name is:" in user_txt and context.user_data["step"] == "update_name": # type: ignore
            name = user_txt.split(":")[1].strip().capitalize()
            # print(name.strip().capitalize())
            print(f"Name is: {name}")
            if name:
                context.user_data["step"] = "finished" # type: ignore
                context.user_data["name"] = name # type: ignore
                await update.message.reply_text("Your name is updated") # type: ignore
            else:
                await update.message.reply_text("Name can't be empty, please repeat the operation") # type: ignore
        else:
            await update.message.reply_text(f"Your text is: {user_txt}, {msg}") # type: ignore
    except Exception as e:
        print(f"Error msg in echo-command, with msg: {e}")

async def update_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        context.user_data["step"] = "update_name" # type: ignore
        await update.message.reply_text("please enter your updated name in this way\n my name is: name here") # type: ignore
    except Exception as e:
        print(f"Error in update-command, with msg: {e}")

async def show_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if context.user_data.get('name', ''): # type: ignore
            await update.message.reply_text(f"Your name is: {context.user_data['name']}") # type: ignore
        else:
            await update.message.reply_text("please update your name first") # type: ignore
    except Exception as e:
        print(f"Error in show_name-command, the msg is: {e}")

def main():
    TOKEN = os.environ.get('TOKEN', 'NULL');

    print(f"Token is: {TOKEN}")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~ filters.COMMAND, echo))
    app.add_handler(CommandHandler("update_name", update_name))
    app.add_handler(CommandHandler("show_name", show_name))

    

    app.run_polling() # type: ignore


if __name__ == '__main__':
    main()