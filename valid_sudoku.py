class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        
        we need to figure out if the sudoku board is valid
        
        first, what is a valid sudoku board? 
        
            each row 1-9 without repetition
            each colmn 1-9
            each square 1-9
            
        JUST checking if valid, not trying to solve it!
        
        so what do we need to check? 
            row
            column
            square
            
        this would mean n*(3n) worth of work to check each of these, which is 
        quadratic time
        
        space is constant
        
        can we do better? 
        
        go through every row and hash
        go through every column and hash
        go through every square and hash
        
        then check to see if valid
        
        that would be n work for each hash so 3*n = O(n)
        then also N memory because O(n) to hold each hashtable, 
        
        squares are 
        0 1 2 
        3 4 5 
        6 7 8
        
        rows are 
        0
        - 
        8
        
        columns
        0 - 8
        """
        
        hashed_rows = {}
        hashed_cols = {}
        hashed_sqrs = {}
        
        # hash rows first 
        for index, val in enumerate(board):
            hashed_rows[index] = {}
            for char in val:
                hashed_rows[index][char] = char
        
        # now hash columns
        for i in range(len(board)):
            
                
            
        
    def add_to_hash(how, seen_numbers, )
        if how == "column":
            
        
        
        
