from urllib import response
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()

def load_history():  
    try:  
        with open("history.json", "r") as file:  
            return json.load(file)  
    except FileNotFoundError:  
        return {}  

def save_history(history):  
    with open("history.json", "w") as file:  
        json.dump(history, file)  

async def rate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        response = requests.get(os.environ.get('url', ''))
        result = response.json()
    except requests.RequestException as e:
        await update.message.reply_text(f'Error in getting rating: {e}') # type: ignore