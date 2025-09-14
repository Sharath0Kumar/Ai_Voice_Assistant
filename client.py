from openai import OpenAI

# pip install openai 

client = OpenAI(
    api_key="Write your api key",
)

completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    message = [
        {"role" : "system", "content": "You are a poetic assistant."},
        {"role" : "user", "content": "Compose a poem that explains the concepts of recussion."},
    ]
)

print(completion.choice[0].message.content)