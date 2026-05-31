import logging
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, filename='logs.log', filemode='a', 
    format='%(asctime)s %(levelname)s %(message)s'
)
load_dotenv()

username = os.environ.get('username', 'None')
print(f'username is: {os.environ.get('bot_username', 'None')}')