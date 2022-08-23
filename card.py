class Card:
    def __init__(self,
        type,
        cost,
        attack=False,
        v_points=0,
        value=0
        ):
        self.cost = cost
        self.type = type   #
        self.attack = attack

        self.v_points = v_points
        self.value = value

    def discard(self):
        # maybe cards can have an owner
        pass