from messaging_strategy import MessagingStrategy
number = input('please enter number(with country code): ')
message = input('type your message: ')


def select_strategy(num):
    if num.startswith('+880'):
        return 'localGateway'
    else :
        return 'twilio'


strategy = select_strategy(number)

message_sender = MessagingStrategy(strategy = strategy)
message_sender.send_sms(message, number)
