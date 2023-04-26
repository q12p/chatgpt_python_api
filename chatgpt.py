#Call this program in terminal with: python chatgpt.py


import openai


openai.api_key= 'WRITE API KEY HERE'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("\n\n\n\n\033[0m User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    
    reply = chat.choices[0].message.content
    print(f"\n\n\n\n\033[96m ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
