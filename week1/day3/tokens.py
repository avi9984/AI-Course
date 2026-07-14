import os;
from pathlib import Path;
from dotenv import load_dotenv;
from groq import Groq;

load_dotenv();

my_api_key=os.getenv("GROK_API_KEY");

if not my_api_key:
    raise ValueError("Api key not found");

client=Groq(api_key=my_api_key);

model="llama-3.3-70b-versatile";

role="user"

#prompt

prompt1="Hi"
prompt2="Explain time travel in details"
prompt3="Write a 1000 word easay in machine learning"

prompts=[prompt1,prompt2,prompt3];

for prompt in prompts:
    message={
    "role":role,
    "content":prompt
}
    messages=[message];

responce=client.chat.completions.create(model=model,messages=messages,max_tokens=50)

usage=responce.usage

print(f"Promt: {prompt} --> your tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens} finish reasion: {responce.choices[0].finish_reason}")
