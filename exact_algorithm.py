from Sudoku import Sudoku


class ExactAlgorithm:
    """ ExactAlgorithm class to implement the exact algorithm """

    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        self.non_perm_cell_index = 0

    def fill_sudoku_with_ones(self):
        """ initial fill sudoku with ones """
        for i, j in self.sudoku.non_perm_cells_list:
            self.sudoku.board[i][j] = 1

    def exact_algorithm(self) -> Sudoku:
        """ exact algorithm implementation """

        # 1. Fill with ones
        self.fill_sudoku_with_ones()

        while True:
            self.non_perm_cell_index = 0

            # 2. Verify
            if self.sudoku.is_valid():
                # 3. If good, return result
                return self.sudoku

            # iterate to new result
            found_cell_not_equal_nine = False
            go_to_next_cell = False
            while not found_cell_not_equal_nine:
                if go_to_next_cell:
                    self.non_perm_cell_index += 1
                    go_to_next_cell = False

                i = self.sudoku.non_perm_cells_list[self.non_perm_cell_index][0]
                j = self.sudoku.non_perm_cells_list[self.non_perm_cell_index][1]

                if self.sudoku.board[i][j] != 9:
                    self.sudoku.board[i][j] += 1
                    found_cell_not_equal_nine = True
                else:
                    self.sudoku.board[i][j] = 1
                    go_to_next_cell = True
