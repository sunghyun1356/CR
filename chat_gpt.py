# 이거 돈내야해서 당장은 사용 ㄴㄴㄴ

import openai
import os
from dotenv import load_dotenv
from .Weather import *
load_dotenv()
openai.api_key = os.getenv('OPENAI.API_KEY')

messages =[]
content = show("남성", "기분이 안좋아요", "좀 깔끔한")
messages.append({"role" : "user", "content": content})
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = messages
)
chat_response = completion.choices[0].message.content
print(f'ChatFPT: {chat_response}')
messages.append({"role": "assistant", "content": chat_response})