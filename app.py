from messaging_strategy import MessagingStrategy
number = input('please enter number(with country code): ')
message = input('type your message: ')


def select_strategy(number):
    if number.startswith('+880'):
        return 'local'
    else :
        return 'twilio'


strategy = select_strategy(number)


message_sender = MessagingStrategy(strategy = strategy)
message_sender.send_sms(message, number)
