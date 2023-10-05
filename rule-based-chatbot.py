import nltk
import random
import time
from datetime import datetime

# Download necessary NLTK data
nltk.download('punkt')

# Define intents and their respective responses
intents = {
    "greet": ["Hello!", "Hi there!", "Hey!"],
    "how_are_you": ["I am good, thanks!", "I'm doing well, how about you?"],
    "what_is_your_name": ["I am a chatbot.", "You can consider me as your Virtual Friend."],
    "what_can_you_do": ["I can answer questions, provide information, and have general conversations."],
    "who_are_you": ["I am a chatbot designed to assist and chat with you."],
    "bye": ["Goodbye!", "See you later!"],
    "help": [
        "You can ask me questions, request information, or just have a chat with me.",
        "I can provide information, answer questions, and engage in casual conversation. Just ask!",
    ],
    "courses": ["Courses offered are: AI/ML, Web Development, Cloud Computing, Android Development"],
    "contact": ["You can contact the developer, Contact details are: Email - farhanmfk5@gmail.com"],
    "weather": ["I cannot provide real-time weather information. You can check a weather website or app for that."],
    "time": "time",
    "date": "date",
    "info": ["Task-1 of Artificial Intellicence Internship","Internship provided by CODSOFT","This is a rule-based ChatBot"],
}

# Function to classify the intent based on the user input
def classify_intent(user_input):
    words = nltk.word_tokenize(user_input.lower())
    for word in words:
        if word in ["hello", "hi", "hey"]:
            return "greet"
        elif word == "bye":
            return "bye"
        elif word in ["how", "are"]:
            return "how_are_you"
        elif word in ["name"]:
            return "what_is_your_name"
        elif word in ["help"]:
            return "help"
        elif word in ["courses"]:
            return "courses"
        elif word in ["contact"]:
            return "contact"
        elif word in ["weather"]:
            return "weather"
        elif word in ["can","do"]:
            return "what_can_you_do"
        elif word in ["who"]:
            return "who_are_you"
        elif word in ["time"]:
            return "time"
        elif word in ["date"]:
            return "date"
        elif word in ["info"]:
            return "info"
    return "unknown"

# Function to respond to user input
def chatbot_response(user_input):
    intent = classify_intent(user_input)
    if intent in intents:
        if intents[intent] == "time":
            current_time = time.strftime("%H:%M:%S")
            return f"The current time is {current_time}."
        elif intents[intent] == "date":
            current_date = datetime.now().strftime("%Y-%m-%d")
            return f"The current date is {current_date}."
        else:
            return random.choice(intents[intent])
    else:
        return "I'm not sure how to respond to that. Please ask questions from the given list."

# Main loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "bye", "goodbye"]:
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
    print()
    print("ASK ME:")
    print("1. How are you")
    print("2. What is your name")
    print("3. What can you do")
    print("4. Who are you")
    print("5. Help")
    print("6. Courses")
    print("7. Contact")
    print("8. Weather")
    print("9. Time")
    print("10. Date")
    print("11. Info")
    print("For ending the coversation type: 'BYE/QUIT' ")
    print()
