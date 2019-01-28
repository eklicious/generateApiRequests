# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Accessing variables.
NUM_REQUESTS = os.getenv('NUM_REQUESTS')
URL = os.getenv('URL')
SECRET = os.getenv('SECRET')
SLEEP_SECONDS = os.getenv('SLEEP_SECONDS')

# Using variables.
print('Num Requests: ' + NUM_REQUESTS)
print('URL: ' + URL)
print('Secret: ' + SECRET)
print('Sleep Seconds: ' + SLEEP_SECONDS)

