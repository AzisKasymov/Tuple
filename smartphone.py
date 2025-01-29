class Smartphone:
    def __init__(self, model, year, size=None):
        self.model = model
        self.year = year
        self.size = size

    def sell(self):
        print('Smartphone', self.model, 'is selling')

    def info(self):
        print('Smartphone model', self.model,'year', self.year, 'size', self.size,)
