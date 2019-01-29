
class MessagingAlgorithm(object):
    def send_sms(self, message, number):
        pass


class TwilioAlgorithm(MessagingAlgorithm):
    def __init__(self):
        super(TwilioAlgorithm, self).__init__()

    def send_sms(self, message, number):
        print('sending through twilio: {} by {}'.format(message, number))


class LocalGatewayAlgorithm(MessagingAlgorithm):

    def __init__(self):
        super(LocalGatewayAlgorithm, self).__init__()

    def send_sms(self, message, number):
        print('sending through local gateway: {} by {}'.format(message, number))
