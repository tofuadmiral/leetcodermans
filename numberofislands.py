class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        2D array of lists of lists, 
        :rtype: int
        """
        
        # count the number of islands
        # can connect horizontally or vertically 
        # all edges are water
        
        
        # run a for loop to step through the list of lists
        
        for i in range(len(grid)): # for each row 
            
            for j in range(len(grid[0])): # for each column in a row 
                
                # if the element is a one, run depth first search on it
                if grid[i][j] == '1':
                    
                    # run a depth first search here

                    # our DFS needs our current position, and our grid of elements
                    depthFirst(i, j, grid)
                else:
                    pass # i.e. go to the next item, keep looking for that one 
                    
            
        