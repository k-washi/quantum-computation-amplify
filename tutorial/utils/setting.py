import os
from dotenv import load_dotenv

def get_amplify_token(dotenv_path):

    load_dotenv(dotenv_path)
    AMPLIFY_TOKEN = os.environ.get("AMPLIFY_TOKEN")
    return AMPLIFY_TOKEN