class Game:
    def __init__(self, _Places):
        self.places = _Places()

    def is_game_over(self):
        gameOver = False

        if self.places.v_cards.provinces == 0:
            gameOver == True
        elif len(self.places.all_piles) <= 14:
            # assuming this includes curses
            gameOver = True

        return gameOver
