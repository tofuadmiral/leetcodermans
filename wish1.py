def most_frequent_character(input):
    seen = {}

    # add to our dictionary

    if not input:
        return ""

    for i in input:
        if i in seen:
            seen[i]+=1
        else:
            seen[i] = 1
    
    return max(seen, key=seen.get)



if __name__ == "__main__":
    testcase1 = 'hello'
    testcase2 = 'asldfiaslkdfjal;skdjf;laksjdflkajsdf;lkjasdlfkjssss'
    testcase3 = ''
    testcase4 = 'asdflaskjdflasjkdflkjiiiieiiiiiiiieee'

    print(most_frequent_character(testcase1))
    print(most_frequent_character(testcase2))
    print(most_frequent_character(testcase3))
    print(most_frequent_character(testcase4))

    
