from Sudoku import Sudoku

GOOD_SOLUTION = [
    (0, 0, 5), (0, 1, 3), (0, 2, 4), (0, 3, 6), (0, 4, 7), (0, 5, 8), (0, 6, 9), (0, 7, 1), (0, 8, 2),
    (1, 0, 6), (1, 1, 7), (1, 2, 2), (1, 3, 1), (1, 4, 9), (1, 5, 5), (1, 6, 3), (1, 7, 4), (1, 8, 8),
    (2, 0, 1), (2, 1, 9), (2, 2, 8), (2, 3, 3), (2, 4, 4), (2, 5, 2), (2, 6, 5), (2, 7, 6), (2, 8, 7),
    (3, 0, 8), (3, 1, 5), (3, 2, 9), (3, 3, 7), (3, 4, 6), (3, 5, 1), (3, 6, 4), (3, 7, 2), (3, 8, 3),
    (4, 0, 4), (4, 1, 2), (4, 2, 6), (4, 3, 8), (4, 4, 5), (4, 5, 3), (4, 6, 7), (4, 7, 9), (4, 8, 1),
    (5, 0, 7), (5, 1, 1), (5, 2, 3), (5, 3, 9), (5, 4, 2), (5, 5, 4), (5, 6, 8), (5, 7, 5), (5, 8, 6),
    (6, 0, 9), (6, 1, 6), (6, 2, 1), (6, 3, 5), (6, 4, 3), (6, 5, 7), (6, 6, 2), (6, 7, 8), (6, 8, 4),
    (7, 0, 2), (7, 1, 8), (7, 2, 7), (7, 3, 4), (7, 4, 1), (7, 5, 9), (7, 6, 6), (7, 7, 3), (7, 8, 5),
    (8, 0, 3), (8, 1, 4), (8, 2, 5), (8, 3, 2), (8, 4, 8), (8, 5, 6), (8, 6, 1), (8, 7, 7), (8, 8, 9),
]


def save_good_solution(solution=GOOD_SOLUTION):
    with open('good_solution.txt', 'w') as f:
        prev_row = solution[0][0]
        for i, j, value in solution:
            if prev_row != i:
                f.write('\n')
            f.write(f"{i} {j} {value}\t")


def get_good_solution():
    good_solution = []
    with open('good_solution.txt', 'r') as f:
        for line in f:
            for part in line.strip().split('\t'):
                i, j, value = map(int, part.split())
                good_solution.append((i, j, value))
    return good_solution


if __name__ == '__main__':
    def test_save_get_solution():
        save_good_solution()
        sudoku = Sudoku(get_good_solution())
        print(sudoku.is_solved())
        print(sudoku.is_valid())
        sudoku.display()
    test_save_get_solution()