def longest_good_segment(bad, interval):

    bad_set = set(bad)

    # keep pointer at last bad number, keep pointer at current number
    last_bad = -1
    longest = 0

    for i in range(len(interval)):
        if interval[i] not in bad_set:
            size = i - last_bad
            if size > longest:
                longest = size
        else:
            last_bad = i
    return longest



if __name__ == "__main__":

    print(longest_good_segment([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


    
