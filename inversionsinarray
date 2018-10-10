// Complete the maxInversions function below.
long maxInversions(vector<int> prices) {
    int size = static_cast<int>(prices.size());
    long inversionSum = 0;
    
    // iterate thru each price
    // determine the max number of inversions
    // brute force: count once thru, count twice thru, count three * 
    // then check to see if we're greater the whole way through
    for (int i=0; i<size; i++){
        for(int j=i+1; j<size; j++){
            for(int k=j+1; k<size; k++){
                
                // check for immediate disqualifiers for inversions
                if(prices[k]>prices[j]){
                    continue;
                }
                
                if(prices[j] > prices[i]){
                    continue;
                }
                
                // check if inversion
                if(prices[k]<prices[j] && prices[j]<prices[i] && prices[k]<prices[i]){
                    // this is an inversion!! val of i > j > k, and index i < j < k
                    inversionSum++;
                } // end if
            }// end third for
        } // end second for
    } // end first for
    return inversionSum;
}

