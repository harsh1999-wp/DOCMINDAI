from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

message_history = []

while True:
    user_input = input("Enter the question you want to ask :")
    
    if(user_input.lower() == 'exit'):
        print("Thank you")
        break

    message_history.append(
        {
            "role":"user",
            "content" :user_input,
        }
    )
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
            "role":"user",
            "content": user_input
            }
        ]
)

    assistant_response = response.choices[0].message.content
    print("\nAI", assistant_response)

    message_history.append(
        {
            "role":"assistant",
            "content":assistant_response,
        }
    )
    print(message_history)
    print("Type exit to comes out of the chat")
