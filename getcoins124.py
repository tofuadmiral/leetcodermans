import sys
for line in sys.stdin:
    fours, twos, ones, coins, rem = 0, 0, 0, 0, 0
    target=int(line)
    if target>=4:
        fours=target/4
        rem=target%4
        if rem>1:
            twos=rem/2
            ones=rem-twos*2
    if target==0:
        print(0)
    if target<4:
        twos=target/2
        ones=target%2
    coins=ones+twos+fours
    print(int(coins)) # cast as an int to get rid of decimals
