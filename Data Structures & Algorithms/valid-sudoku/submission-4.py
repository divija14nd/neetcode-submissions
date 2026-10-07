class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        dup = set()
        rl = len(board)
        cl = len(board[0])
        res = True


        for i in range(rl):
            dup.clear()
            for j in range(cl):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in dup:
                    res = False
                else:
                    dup.add(board[i][j])
                  
        
        for i in range(cl):
            dup.clear()
            for j in range(rl):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in dup:
                    res = False
                else:
                    dup.add(board[j][i])
                    

        dup.clear()

     

        for br in range(0,9,3):
            for bc in range(0,9,3):
                dup.clear()
                for k in range(3):
                    for l in range(3):
                        v = board[br+k][bc+l]
                        if v == ".":
                            continue
                        if v in dup:
                            return False
                        dup.add(v)
                    

        return res
                

    


                



  

