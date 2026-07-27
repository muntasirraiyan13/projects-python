import google.generativeai as genai

genai.configure(api_key="API_KEY_HERE")

model = genai.GenerativeModel('gemini-3.6-flash')

chat = model.start_chat(history=[])

print("Chatbot is ready! Type 'quit' to exit.")
print("-" * 40)

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        print("Chatbot: Goodbye!")
        break
        
    response = chat.send_message(user_input)
    
    print(f"Chatbot: {response.text}")
