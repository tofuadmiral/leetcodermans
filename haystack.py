'''
function int[] grep(string haystack, string needle)
haystack = "aaabcdddbbddddabcdefghi"
needle = "abc"
[2,14]

two pointer system
    one starts at the beginning
    other pointer starts at previous pointer, and goes to end
    
    for i in range(len(haystack))
        for j in in range(i, len(haystack), 3)
                for i in range(start, end)
                    haystakc[start] == needle 
'''

def grep(haystack, needle):
    
    if not haystack:
        return []
    
    if not needle:
        return []
    
    if len(needle) > len(haystack):
        return []
    
    occurences = []
    
    for i in range(len(haystack)):
        if(i+len(needle)) > len(haystack):
            break
        for j in range(i, i+len(needle)):
            if haystack[j] != needle[j-i]:
                break 
            if (j == (i + len(needle)-1)):
                occurences.append(i)
    
    return occurences 


needle = ""

haystack = "aaaaa"

print(grep(haystack, needle))

