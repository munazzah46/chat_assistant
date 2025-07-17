import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of questions and answers
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name ?",
        ["I'm CodBot, your internship assistant."]
    ],
    [
        r"how are you ?",
        ["I'm doing great, thank you!"]
    ],
    [
        r"(.*) (created|made) you ?",
        ["I was created by a CodTech intern using Python and NLTK."]
    ],
    [
        r"what is NLP ?",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."]
    ],
    [r"who are you ?", ["I'm your friendly chatbot for the CodTech internship."]],
    [r"what can you do ?", ["I can answer your questions and help you understand NLP basics."]],
    [r"how does NLP work ?", ["NLP processes and analyzes human language so machines can understand it."]],
    [r"what is CodTech ?", ["CodTech is an online internship and training platform."]],
    [r"thank you", ["You're welcome!", "Happy to help!"]],
    [
        r"quit",
        ["Goodbye! Have a nice day."]
    ]
]

# Create a chatbot function
def codtech_chatbot():
    print("Hi! I’m CodBot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Run the chatbot
codtech_chatbot()
