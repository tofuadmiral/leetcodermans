int mySqrt(int x) {
   //  // base cases of 0 and 1 sqrt
   // if (x == 0 || x == 1){
   //     return x;
   // }
   //  int i = 0;
   //  int product = 0;
   //  while (product <= x){
   //      i++;
   //      product = i*i;
   //  }
   //  return i-1;
    
    
    // try a binary search solution to the square root
    // use a long so we don't overflow the integer if we're close to max int
    long left = 0;
    long right = x;
    long mid;
    while (left<=right){
        mid = (left+right)/2;
        if (mid * mid > x)
            right = mid-1;
        if (mid * mid < x)
            left = mid +1;
        if (mid *mid == x)
            return mid;
    }
    return left-1;
}