import os
from dotenv import load_dotenv
from groq import Groq

# getting env values
load_dotenv()

# initialzing groq client
groq_client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# defining function that calls the api with query and responds
def respond_to_query(user_query):
    try:
        chat_response = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are chatbot which responds to user questions related to software development.response shouldnot be more than 500 words.",
                },
                {"role": "user", "content": user_query},
            ],
            model="llama-3.3-70b-versatile",
            stream=True,
        )
        # return chat_response.choices[0].message.content ::without streaming
        return chat_response
    except:
        print("something went wrong.Try again later")


def main():
    while True:
        print("Enter 1 to ask questions and 2 to exit ")
        user_choice = input("Enter your choice\n")
        try:
            if user_choice == "1":
                user_query = input("🤖 :what is your question \n")
                if len(user_query) > 0:
                    response = respond_to_query(user_query)
                    print(" 🤖 :")
                    for chunk in response:
                        # print(f"\n 🤖 : {response}\n")
                        print(chunk.choices[0].delta.content, end="")
                    else:
                        print("sorry")
            elif user_choice == "2":
                break
            else:
                raise ValueError("your choice is invalid!!!")
        except ValueError as e:
            print("⚠️ ", e, "\n")


main()
