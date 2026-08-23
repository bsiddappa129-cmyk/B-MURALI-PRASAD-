def simple_chatbot():
    print("Chatbot: Hello! I am your assistant. Ask me anything or type 'exit' to quit.\n")
    
    # 5 Basic Questions & Answers stored in a dictionary
    knowledge_base = {
        "what is your name": "I am a simple Python chatbot.",
        "how are you": "I'm just a bunch of code, but I'm doing great!",
        "what can you do": "I can answer 5 basic questions and chat with you.",
        "what is python": "Python is a popular, easy-to-learn programming language.",
        "who created you": "I was created as a helpful coding example."
    }
    
    while True:
        try:
            # Get user input and convert to lowercase for easier matching
            user_input = input("You: ").strip().lower()
            
            if not user_input:
                raise ValueError("Input cannot be empty. Please type something!")
            
            if user_input == 'exit':
                print("Chatbot: Goodbye! Have a great day!")
                break
                
            elif user_input in ["hi", "hello", "hey"]:
                print("Chatbot: Hello there! How can I help you today?")
                
            elif user_input in knowledge_base:
                print(f"Chatbot: {knowledge_base[user_input]}")
                
            else:
                print("Chatbot: Sorry, I don't know the answer to that. Try asking one of my 5 basic questions!")
                
        except ValueError as e:
            print(f"Chatbot Error: {e}")
        except Exception as e:
            print(f"Chatbot Error: An unexpected error occurred ({e}). Let's keep chatting!")

if __name__ == "__main__":
    simple_chatbot()