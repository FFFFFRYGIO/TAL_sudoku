from Sudoku import Sudoku, Cell


class ExactAlgorithm:
    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        self.i_index = self.j_index = 0

    def fill_sudoku_with_ones(self):
        """ initial fill sudoku with ones """
        for i in range(9):
            for j in range(9):
                if not self.sudoku.board[i][j].is_perm:
                    self.sudoku.board[i][j].value = 1

    def increment_indexes_to_another_non_perm_cell(self, check_at_start=False):
        """ get indexes to another non-perm cell """

        if check_at_start and not self.sudoku.board[self.i_index][self.j_index].is_perm:
            return

        do_while_mod = True
        while do_while_mod:

            self.j_index += 1

            if self.j_index > 8:  # next row
                self.j_index = 0
                self.i_index += 1
                if self.i_index > 8:
                    raise ValueError('ExactAlgorithm: cells exhausted during decrease_indexes')

            if not self.sudoku.board[self.i_index][self.j_index].is_perm:
                do_while_mod = False

    def exact_algorithm(self):

        # 1. Fill with ones
        self.fill_sudoku_with_ones()

        while True:

            # reset indexes
            self.i_index = self.j_index = 0

            # 2. Verify
            if self.sudoku.is_valid():
                # 3. If good, return result
                return self.sudoku

            # Catch next non-perm cell
            while self.sudoku.board[self.i_index][self.j_index].is_perm:
                self.increment_indexes_to_another_non_perm_cell(check_at_start=True)

            # iterate to new result
            found_cell_not_equal_nine = False
            go_to_next_cell = False
            while not found_cell_not_equal_nine:
                if go_to_next_cell:
                    self.increment_indexes_to_another_non_perm_cell()
                    go_to_next_cell = False

                if self.sudoku.board[self.i_index][self.j_index].value != 9:
                    # on tu iteruje wszystkie do 9, ale nie resetuje wartości!!!!
                    self.sudoku.board[self.i_index][self.j_index].value += 1
                    found_cell_not_equal_nine = True
                else:
                    self.sudoku.board[self.i_index][self.j_index].value = 1
                    go_to_next_cell = True
