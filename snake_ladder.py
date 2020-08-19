import random


class Input:

    def input_turns(self):
        turns = input("Enter no of turns to play e.g. 10 (max 100)")
        if turns.isdigit() and int(turns) <= 100:
            return turns
        else:
            print("Please enter valid integer for turns")
            self.input_turns()


class SnakeLadder:

    def __init__(self, snake_positions):
        self.player_position = 1
        self.snake_positions = {position[0]: position[1] for position in snake_positions}

    @staticmethod
    def get_dice_value():
        return random.randrange(1, 6)

    def start_game(self, turns):
        while turns > 0:
            dice_value = SnakeLadder.get_dice_value()
            self.player_position += dice_value
            if self.snake_positions.get(self.player_position):
                self.player_position = self.snake_positions.get(self.player_position)


def main():
    print("Welcome to Snakes and Ladders!!!!!!!")
    inp = Input()
    turns = inp.input_turns()
    snake_positions = input("Enter snake positions comma separated e.g. 31, 40, 58, 65")
    input("Press Enter to continue......")

    SnakeLadder(snake_positions).start_game(turns)


if __name__ == '__main__':
    main()
