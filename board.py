class Board:

    def __init__(self):
        self.array = []

        self.array.append(0b00011100)
        self.array.append(0b00011100)
        self.array.append(0b01111111)
        self.array.append(0b01110111)
        self.array.append(0b01111111)
        self.array.append(0b00011100)
        self.array.append(0b00011100)

        self.DIR_NORTH = 3
        self.DIR_SOUTH = 4
        self.DIR_EAST = 1
        self.DIR_WEST = 2


    def get_position(self, x, y):
        mask = 1 << (6-x)
        testValue = self.array[y] & mask
        if testValue > 0:
            return 1
        else:
            return 0


    def set_position(self, x, y, value):
        if value == 1:
            mask = 1 << (6-x)
            self.array[y] = self.array[y] | mask
        if value == 0:
            mask = ~(1 << (6-x))
            self.array[y] = self.array[y] & mask


    def print_board(self):
        for i in range(7):
            print format(self.array[i], '07b')

    def create_copy(self):
        board = Board()
        board.array[0] = self.array[0]
        board.array[1] = self.array[1]
        board.array[2] = self.array[2]
        board.array[3] = self.array[3]
        board.array[4] = self.array[4]
        board.array[5] = self.array[5]
        board.array[6] = self.array[6]
        return board

    def inside_board(self, x, y):
        outside_board = x < 0 or x > 6 or y < 0 or y > 6
        in_left_upper = x < 2 and y < 2
        in_right_upper = x > 4 and y < 2
        in_left_lower = x < 2 and y > 4
        in_right_lower = x > 4 and y > 4

        if in_left_upper or in_left_lower or in_right_lower or in_right_upper or outside_board:
            return False

        return True
