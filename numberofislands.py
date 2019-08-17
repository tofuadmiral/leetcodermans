class Solution:
    
    def depthFirst(self, i, j, grid):
        # this is our function that will perform the depth first search 
        # we can change grid value as we visit to make it a 


        # check if we're at a valid position
        if i >= len(grid) or i < 0:
            return
        if j >= len(grid[0]) or j < 0:
            return

        # if the current node is a zero, we don't have to visit it
        if grid[i][j] == '0':
            return

        # mark current node as visited, i.e. make it a zero
        if grid[i][j] == '1':
            # mark it as a zero
            grid[i][j] = '0'

        
        # will only reach this if the element is a 1 and not at the edge
        left = j-1
        right = j+1
        up = i-1
        down = i+1

        self.depthFirst(up, j, grid)
        self.depthFirst(down, j, grid)
        self.depthFirst(i, left, grid)
        self.depthFirst(i, right, grid)

    def numIslands(self, grid):
        counter = 0
        for i in range(len(grid)): # for each row 
            
            for j in range(len(grid[0])): # for each column in a row 
                
                # if the element is a one, run depth first search on it
                if grid[i][j] == '1':
                    
                    # run a depth first search here
                    # our DFS needs our current position, and our grid of elements

                    self.depthFirst(i, j, grid)
                    counter+=1 # since we did a depth first, we found the associated island! 
                else:
                    pass # i.e. go to the next item, keep looking for ones
        return counterx