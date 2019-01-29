
class AlgorithmFactory(object):

    @staticmethod
    def create_algorithm(name):
        target_class = name[:1].upper()+name[1:]+'Algorithm'
        return globals()[target_class]()
