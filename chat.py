import os
import google.generativeai as genai

# Replace with your actual API key
my_api_key = "AIzaSyAXII413W1cHh3tqlzlX8k34J3Ehrzcw9s"

# Configure the API key
genai.configure(api_key=my_api_key)


# Create the model
generation_config = {
  "temperature": 0,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash",
  generation_config=generation_config,
  system_instruction="You're a tourist guide, when people visits you...you're going to assist them clearly about the tourist spots and what are the exquisist spots near that user, you're supposed to be a wholesome tourist guide, dont give an essay straightaway, answer the user minimal, making the chat interactable\n",
)

history=[]
print("Yathra: Hello, how can i help you?")
while True:

    user_input = input("You:")
    chat_session = model.start_chat(
    history=history
    )
    
    response = chat_session.send_message(user_input)


    model_response = response.text

    print(f'Yathra: {model_response}')
    print()

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role" : "model", "parts": [model_response]})

