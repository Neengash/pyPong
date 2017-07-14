class Scene():

    def loop(self, state):
        self.check_inputs(state)
        self.update(state)
        self.draw(state)

    def check_inputs(self, state):
        pass

    def update(self, state):
        pass

    def draw(self, state):
        pass
