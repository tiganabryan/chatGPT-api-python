from dotenv import load_dotenv

load_dotenv()

import os
import openai

openai.api_key = os.getenv("openai_api_key")

openai.Model.list()

model_engine = "text-davinci-003"
prompt = input("ask a question: ")

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=1,
)

response = completion.choices[0].text
print(response)
