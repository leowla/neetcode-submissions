class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit != ".":
                    # treat boxes as its own 3x3 grid
                    box_row = row // 3
                    box_col = col // 3
                    # the box row,col pattern can form a base3 number
                    box_index = box_row * 3 + box_col
                    if digit in rows[row] or digit in cols[col] or digit in boxes[box_index]:
                        return False
                    rows[row].add(digit)
                    cols[col].add(digit)
                    boxes[box_index].add(digit)
        return True