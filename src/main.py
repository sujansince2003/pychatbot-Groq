import os
from dotenv import load_dotenv
from groq import Groq


# getting env values
load_dotenv()

# initialzing groq client

groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


def respond_to_query(user_query):
    try:
        chat_response = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": user_query}],
            model="llama-3.3-70b-versatile",
        )
        return chat_response.choices[0].message.content
    except:
        print("something went wrong.Try again later")


def main():
    while True:
        print("Enter 1 to ask questions and 2 to exit ")
        user_choice = int(input("Enter your choice\n"))

        if user_choice == 1:
            user_query = input("🤖 :what is your question \n")
            if len(user_query) > 0:
                response = respond_to_query(user_query)
                print(f"\n 🤖 : {response}\n")
            else:
                print("sorry")
        else:
            break


main()
