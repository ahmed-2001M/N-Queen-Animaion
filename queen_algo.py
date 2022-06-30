import pygame as pg
import numpy as np


class queen:

    def __init__(self, n):
        self.n = n

        self.board = np.zeros((n, n))

    # ------------------------------------------------------------------------------------------------------------

    def validate(self, row, col):

        for i in range(col):
            if self.board[row][i] == 1:
                return False

            # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

            # Check lower diagonal on left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    # --------------------------------------------------------------------------------------------------------
    def print(self):
        for i in range(self.n):
            print(self.board[i])


   #---------------------------------------------------------------------------------------------------------
    def back_track(self, screen, queen, sq_size, col):
        if col >= self.n:
            return True

        for row in range(self.n):

            if self.validate(row, col):

                self.board[row][col] = 1.0

                if self.back_track(screen, queen, sq_size, col + 1) == True:
                    return True

                self.board[row][col] = 0.0

        return False

    # ---------------------------------------------------------------------------------------------------------

