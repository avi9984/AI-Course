import os;
from pathlib import Path;
from dotenv import load_dotenv;
from groq import Groq;

load_dotenv();
my_api_key=os.getenv("GROK_API_KEY");

if not my_api_key:
    raise ValueError("API key not found");

client=Groq(api_key=my_api_key);

model="llama-3.3-70b-versatile";

role="user"

# prompt="I love you baby";
prompt="Suggest a name for my food company"

message_system={
    "role":"system",
    # "content":"You are my loving girlfriend"
    # "content":"You are my strict office colleague who is also my manager"
    "content":"You are a brand manager who suggests name for my food company. name should be in one word"
}

message={
    "role":role,
    "content":prompt
}

messages=[message_system,message];

responce=client.chat.completions.create(model=model,messages=messages,temperature=2)

answer=responce.choices[0].message.content

print(answer)