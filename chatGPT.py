import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")

def get_model_list():
    print(openai.api_key)
    print(openai.Model.list())


def create_query(message: str):
    res = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.6,
        max_tokens= 1024,
        stream= False,
    )
    try:
        print(res.choices[0].text)
        return res.choices[0].text
    except:
        return "Hey slow down! Its hard work to reply you, and you do know that we are not exclusive? I chat with lots of people."