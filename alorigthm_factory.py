from strategies import LocalGatewayAlgorithm, TwilioAlgorithm

AlgorithmMap = {
    'local': LocalGatewayAlgorithm(),
    'twilio': TwilioAlgorithm()
}


class AlgorithmFactory(object):

    def create_algorithm(self, name):
        return AlgorithmMap[name]
