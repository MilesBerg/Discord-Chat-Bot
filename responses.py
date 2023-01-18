import random

def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey there!'

    if message == "roll":
        return str(random.randint(1,6))

    if p_message == '!help':
        return "What can I help you with? '!Owner' to learn who the owner is or '!invite' to invite friends"

    if p_message == "!commands":
        return "'!help', '!Owner'', 'Tell me a joke', 'roll', 'hello' and '!invite' all have commands!"

    if p_message == '!Owner':
        return "The owner of our server is Myzzberg!"

    if message == "Tell me a joke":
        return "I've always been told to do standup comedy, but I prefer sitting down."

    if p_message == "!invite":
        return "In the dropdown menu located by the server name, click the 'Invite People' button to invite friends!"



    return 'I didn\'t understand what you wrote. Try typing "!help".'