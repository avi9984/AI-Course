import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROK_API_KEY")

if not my_api_key:
    raise ValueError("API key not found");

client=Groq(api_key=my_api_key)

model="llama-3.3-70b-versatile";
role="user";
promt="Do you know Sonam Wangchuk?";
#message me role and cotent

message={
    "role":role,
    "content":promt
}

messages=[message];

responce=client.chat.completions.create(model=model,messages=messages)

# print(responce)

print("###############################")

answer=responce.choices[0].message.content
print(answer)
