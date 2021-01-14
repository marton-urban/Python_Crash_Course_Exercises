messages = ['Ez egy sms.', 'Ez még egy fucking sms.', 'Faszom, ez még mindig egy kiba sms.']
sent_messages = []


def send_messages():
    """Print each message and move to another list"""
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)


send_messages()
print(messages)
print(sent_messages)
