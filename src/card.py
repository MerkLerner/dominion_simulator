class Card:
    def __init__(self,
        type,
        cost,
        attack=False,
        reaction=False,
        v_points=0,
        value=0
        ):
        self.cost = cost
        self.type = type   #
        self.attack = attack

        self.v_points = v_points
        self.value = value

    def __repr__(self) -> str:
        return self.__class__.__name__