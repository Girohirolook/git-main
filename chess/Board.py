from Figures import *


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        self.field.append([Rook(0, 0, WHITE), Knight(0, 1, WHITE), Bishop(0, 2, WHITE), Queen(0, 3, WHITE),
                           King(0, 4, WHITE), Bishop(0, 5, WHITE), Knight(0, 6, WHITE), Rook(0, 7, WHITE)])
        self.field.append([Pawn(1, 0, WHITE), Pawn(1, 1, WHITE), Pawn(1, 2, WHITE), Pawn(1, 3, WHITE),
                           Pawn(1, 4, WHITE), Pawn(1, 5, WHITE), Pawn(1, 6, WHITE), Pawn(1, 7, WHITE)])
        for i in range(4):
            self.field.append([None] * 8)
        self.field.append(
            [Pawn(6, 0, BLACK), Pawn(6, 1, BLACK), Pawn(6, 2, BLACK), Pawn(6, 3, BLACK), Pawn(6, 4, BLACK),
             Pawn(6, 5, BLACK), Pawn(6, 6, BLACK), Pawn(6, 7, BLACK)])
        self.field.append(
            [Rook(7, 0, BLACK), Knight(7, 1, BLACK), Bishop(7, 2, BLACK), Queen(7, 3, BLACK), King(7, 4, BLACK),
             Bishop(7, 5, BLACK), Knight(7, 6, BLACK), Rook(7, 7, BLACK)])

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def is_under_attack(self, row, col, color):
        for i in self.field:
            for figure in i:
                if figure and figure.get_color() == color:
                    if figure.can_move(row, col):
                        return True
        return False

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = (self.color + 1) % 2
        return True
