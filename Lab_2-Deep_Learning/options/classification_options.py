from options.options import Options


class ClassificationOptions(Options):
    def __init__(self):
        super().__init__()
        # dataset related
        self.batch_size_test = 10
        self.batch_size_train = 64

        # hyperparameters
        self.lr = 0.012
        self.num_epochs = 10
        self.hidden_sizes = [784, 550, 150, 10]
