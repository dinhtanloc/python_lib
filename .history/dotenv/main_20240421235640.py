import os
from dotenv import load_dotenv

load_dotenv()

DB_host=os.getenv('HOST')
API_key=os.getenv('API_key')