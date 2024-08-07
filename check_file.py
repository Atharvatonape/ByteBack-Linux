import os
from dotenv import load_dotenv

load_dotenv()
PATH = os.getenv("UNIQUE_TEST_FOLDER", "")

def file_validate(history_file):
    for file in os.listdir(PATH):
        # print(file)
        if file == history_file:
            # print("File found")
            return True, None
    return False

#val= file_validate("pdf (1).jpg")
# print(val, name)