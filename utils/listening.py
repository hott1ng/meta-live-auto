import os
from dotenv import load_dotenv

load_dotenv()

def start_listening():
    path = os.getenv("BINARY_LOCATION")
    os.system(f"{path} --remote-debugging-port=9222")

if __name__ == '__main__':
    start_listening()
