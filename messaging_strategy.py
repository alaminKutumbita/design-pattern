from alorigthm_factory import AlgorithmFactory


class MessagingStrategy(object):

    def __init__(self, strategy='local'):
        self.strategy_selected = AlgorithmFactory().create_algorithm(name=strategy)

    def send_sms(self, message, number):
        self.strategy_selected.send_sms(message, number)
