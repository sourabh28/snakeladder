import random


class Input:

    def input_turns(self):
        turns = input("Enter no of turns to play e.g. 10 (max 100):")
        try:
            return int(turns)
        except:
            print("Please enter valid integer for turns:")
            self.input_turns()

    def input_dice_type(self):
        dice_type = input("select dice N for normal, C for Crooked:")
        if dice_type in ('N', 'C'):
            return dice_type
        else:
            print("Please input valid dice type (N/C)")
            self.input_dice_type()

    def input_snake_positions(self):
        snake_positions = input("Enter snake positions (start, end) comma separated e.g. (31,8), (40,12):")
        try:
            start_end_positions = eval(snake_positions)
            for position in start_end_positions:
                if isinstance(position, tuple) and (position[0] > position[1]) and int(position[0]) < 100:
                    return eval(snake_positions)
                else:
                    print("Please input valid snake positions in format mentioned e.g. [(31,8), (40,12)]")
                    self.input_snake_positions()
        except:
            print("Please input valid snake positions in format mentioned e.g. [(31,8), (40,12)] not exceeding 99")
            self.input_snake_positions()


class SnakeLadder:

    def __init__(self, snake_positions):
        self.player_position = 1
        self.snake_positions = {position[0]: position[1] for position in snake_positions}

    @staticmethod
    def get_dice_value(dice_type):
        return random.randrange(1, 6) if dice_type == 'N' else random.choice([2, 4, 6])

    def update_player_position(self, dice_value):
        self.player_position += dice_value
        if self.snake_positions.get(self.player_position):
            self.player_position = self.snake_positions.get(self.player_position)

    def start_game(self, turns, dice_type):
        while turns > 0:
            dice_value = SnakeLadder.get_dice_value(dice_type)
            self.update_player_position(dice_value)
            print("Player moved to:" + str(self.player_position))
            turns -= 1
        print("Game end!!! Exit")


def main():
    print("Welcome to Snakes and Ladders!!!!!!!")
    inp = Input()
    turns = inp.input_turns()
    dice_type = inp.input_dice_type()
    snake_positions = inp.input_snake_positions()
    input("Press Enter to continue......")

    SnakeLadder(snake_positions).start_game(turns, dice_type)


if __name__ == '__main__':
    main()


def test_if_player_position_initialized():
    self = SnakeLadder(snake_positions=[(31, 5)])
    assert self.player_position == 1


def test_player_position_if_snake_present():
    turns = 6
    self = SnakeLadder(snake_positions=[(31, 5)])
    while turns > 0:
        dice_value = 5
        self.update_player_position(dice_value)
        turns -= 1
    assert self.player_position == 5


def test_player_position_if_snake_absent():
    turns = 6
    self = SnakeLadder(snake_positions=[(20, 5)])
    while turns > 0:
        dice_value = 4
        self.update_player_position(dice_value)
        turns -= 1
    assert self.player_position == 25


def test_crooked_dice_value():
    assert SnakeLadder.get_dice_value('C') % 2 == 0

