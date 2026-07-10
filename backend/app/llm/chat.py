from llm.client import client
from llm.prompt import SYSTEM_PROMPT

message_history = [
    {
        "role":"system",
        "content": SYSTEM_PROMPT,
    }
]

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
        messages=message_history,
        stream = True,    
    )

    assistant_response = ""

    print("\nAI: ", end="", flush=True)

    for chunk in response:
        token = chunk.choices[0].delta.content

        if token :
            print(token, end="" , flush = True)   
            assistant_response += token
    
    #print("\nAI", assistant_response)
    print()

    message_history.append(
        {
            "role":"assistant",
            "content":assistant_response,
        }
    )
    if DeBUG:
    print("\nConversation History:")
    for msg in message_history:
        print(f"{msg['role']}: {msg['content']}")

    print("Type exit to comes out of the chat")

