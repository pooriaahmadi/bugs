from Game.Game import Game


class Main:
    """
    Doing nerd stuff for making the code look sick
    """

    def __init__(self):
        self.game = Game(window_name="Bugs")
        self.game.initiate()
        self.game.run()


if __name__ == "__main__":
    Main()
