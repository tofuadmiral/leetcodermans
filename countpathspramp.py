def num_of_paths_to_dest(n):
  pass # your code goes here

  # breadth first solution 
  # i can never be > j
  
  numpaths=0
  recursiveFunction(numpaths, 0, 0)
  
  visitedNodes=[n][n]

    
def recursiveFunction(numpaths, i, j):
   if(visitedNodes[i,j]==1):
    return
  
  validright=(j+1)<n
  validup=j>=i+1
  
  
  # invalid right movement
  if (!validright):
    return
  
  if (!validup):
    return
  
  #move right 0,5 
  recursiveFunction(numpaths, i, j+1) 
  
  #move up  
  recursiveFunction(numpaths, i+1, j)
  
  visitedNodes[i][j]=1
  
  # base case
  if(i==(n-1) and j==(n-1)):
    numpaths+=1
  
