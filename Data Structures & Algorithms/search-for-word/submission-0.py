class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        rows, cols = len(board), len(board[0])
        res = False
        def backtrack(i, j, seen, start):
            if start == len(word):
                return True

            for dr, dc in directions:
                nr, nc = dr + i, dc + j
                
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == word[start] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    if backtrack(nr, nc, seen, start+1):
                        return True
                    seen.remove((nr, nc))

            return False
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if backtrack(i, j, {(i, j)}, 1):
                        return True
        
        return False