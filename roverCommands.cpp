/*
 * Complete the 'roverMove' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER matrixSize
 *  2. STRING_ARRAY cmds
 */

int roverMove(int matrixSize, vector<string> cmds) {
    int numCmds = static_cast<int>(cmds.size());
    
    // matrix size is how many elements in rows/cols, square matrix
    // then DIVIDE TO GET row number, MOD to get col number
    
    int currpos = 0; // our current position
    
    for(int i = 0; i<numCmds; i++){
        // iterate over the number of cmds
        
        // four cases
        
        if(cmds[i] == "UP"){
            // check for upwards edge 
            if(currpos<matrixSize){
                // can't go up bc there's an edge
                continue; // go to next command
            }
            else{
                // we can go up one, so that means subtract 
                currpos -= matrixSize;
            }
        }
        
        if(cmds[i] == "DOWN"){
             // check for downwards edge 
            if(currpos>=(matrixSize*matrixSize-matrixSize)){
                // can't go down bc there's an edge
                continue; // go to next command
            }
            else{
                // we can go down one, so that means add matrixSize 
                currpos+=matrixSize;
            }
        }
        
        if(cmds[i] == "RIGHT"){
            // check for rightwards edge 
            if((currpos+1)%matrixSize == 0){
                // can't go right bc there's an edge
                continue; // go to next command
            }
            else{
                // we can go right, so add one 
                currpos++;
            }
        }
        
        if(cmds[i] == "LEFT"){
            // check for rightwards edge 
            if((currpos)%matrixSize == 0){
                // can't go left bc there's an edge
                continue; // go to next command
            }
            else{
                // we can go left, so subtract one 
                currpos--;
            }
            
         }
    }
    return currpos;
}

