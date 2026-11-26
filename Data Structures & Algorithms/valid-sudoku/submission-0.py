class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                num = board[i][j]
                # forger to jump .
                if num == ".":
                    continue

                if num not in rows[i]:
                    rows[i].add(num)
                else:
                    return False
                if num not in cols[j]:
                    cols[j].add(num)
                else:
                    return False
                box_num = (i // 3) * 3 + j // 3
                if num not in box[box_num]:
                    box[box_num].add(num)
                else:
                    return False
        return True