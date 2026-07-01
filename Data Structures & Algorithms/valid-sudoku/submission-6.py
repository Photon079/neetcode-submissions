class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checking duplicate elements in each row
        for row in board:
            seen=set()
            for cell in row:
                if cell!=".":
                    if cell in seen:
                        return False 
                    seen.add(cell)
        #checkin douplicate elements in each column
        for row in range(9):
            seen = set()
            for col in range(9):
                cell=board[col][row]
                if cell!=".":
                    if cell in seen:
                        return False
                    seen.add(cell)
        #checking duplictaes inside a box 
        for box_row in (0,3,6):
            for box_col in(0,3,6):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        c=board[box_row+i][box_col+j]
                        if c!=".":
                            if c in seen:
                                return False
                            seen.add(c)
        #if all of these checks pass, then  no duplicates
        return True

        


