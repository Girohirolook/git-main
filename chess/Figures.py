WHITE = 0
BLACK = 1


class Base:
    def __init__(self, row, col, color):
        self.color = color
        self.row = row
        self.col = col

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color


class Bishop(Base):
    def char(self):
        return 'B'

    def can_move(self, row1, col1):
        if row1 > 7 or row1 < 0 or col1 > 7 or col1 < 0:
            return False
        moves = []
        for i in range(1, 8):
            moves.append((self.row - i, self.col + i))
            moves.append((self.row - i, self.col - i))
            moves.append((self.row + i, self.col + i))
            moves.append((self.row + i, self.col - i))
        if (row1, col1) in moves:
            return True


class King(Base):
    def char(self):
        return 'K'

    def can_move(self, row1, col1):
        moves = [(self.row + 1, self.col),
                 (self.row + 1, self.col + 1),
                 (self.row - 1, self.col),
                 (self.row - 1, self.col - 1),
                 (self.row + 1, self.col - 1),
                 (self.row - 1, self.col + 1),
                 (self.row, self.col + 1),
                 (self.row, self.col - 1)]
        if (row1, col1) in moves:
            return True


class Knight(Base):
    def char(self):
        return 'N'

    def can_move(self, row1, col1):
        if row1 > 7 or row1 < 0 or col1 > 7 or col1 < 0:
            return False
        moves = [(self.row + 2, self.col - 1),
                 (self.row + 2, self.col + 1),
                 (self.row - 2, self.col - 1),
                 (self.row - 2, self.col + 1),
                 (self.row + 1, self.col + 2),
                 (self.row - 1, self.col + 2),
                 (self.row + 1, self.col - 2),
                 (self.row - 1, self.col - 2)]
        if (row1, col1) in moves:
            return True


class Pawn(Base):
    def char(self):
        return 'P'

    def can_move(self, row, col):
        if self.col != col:
            return False
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if self.row + direction == row:
            return True
        if self.row == start_row and self.row + 2 * direction == row:
            return True
        return False


class Queen(Bishop):
    def char(self):
        return 'Q'

    def can_move(self, row1, col1):
        if row1 == self.row or col1 == self.col:
            return True
        return super().can_move(row1, col1)


class Rook(Base):
    def char(self):
        return 'R'

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True
