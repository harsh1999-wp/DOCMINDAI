from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY
from langchain_core.messages import SystemMessage , HumanMessage 
from langchain_core.prompts import ChatPromptTemplate 
#user_input = input("Enter the sentence You want to translate :")
#language = input("Which language you want to translate to")
#system_input = f"""you are helpful assistant that translate English  to {language} . Translate the user sentence"""


llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature= 0,
    max_tokens = None,
    timeout = None,
    max_retries = 2,
)

template = ChatPromptTemplate.from_messages(
    [   
        ("system" , "You are helpful AI bot . Your name is {name}"),
        ("human" , "Hello , how  are you doing"),
        ("ai",  "I'm doing well, thanks!"),
        ("human" , "{user_input}"),
    ]
)

travel_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an experienced travel planner named {name}."
        ),
        (
            "human",
            """
I want to travel.

Source: {source}
Destination: {destination}
Days: {days}

Please suggest:
1. Best mode of transport
2. Estimated budget
3. Places to visit
4. A day-wise itinerary
"""
        )

    ]
)
name = input("Enter planner name: ")
source = input("Enter source city: ")
destination = input("Enter destination city: ")
days = input("Enter number of days: ")


# ---------------------------
# Create Prompt
# ---------------------------
prompt = travel_template.invoke(
    {
        "name": name,
        "source": source,
        "destination": destination,
        "days": days,
    }
)
#messages = [
 #   SystemMessage(content = system_input),
  #  HumanMessage(content =  user_input)
#]

#ai_msg = llm.invoke(messages)
#ai_msg
#print(type(ai_msg))
#print(ai_msg)
#print("\n Response")
#print(ai_msg.content)
#print(prompt_value.messages)
#response = llm.invoke(prompt_value)
#print(response)

print("Generated Messages:\n")
for msg in prompt.messages:
    print(msg)
    print("-" * 50)

# Send the completed prompt to the LLM
response = llm.invoke(prompt)

# Print the AI response
print("\nAI Response:\n")
print(response.content)