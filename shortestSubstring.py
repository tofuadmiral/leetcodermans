def get_shortest_unique_substring(arr, str):
  # first check if we have all the characters in arr, if we don't, don't process, just return 
  # the empty string 

  ar={}

  for i in arr:
    ar[i]=1

  for i in range(len(str)):
    ar[str[i]]=0

  valsum=0
  for i in ar.values():
    valsum+=i

  if valsum!=0: return ""


  # now that we know we have all the charaters in arr, try our solution 

  for i in arr:
    ar[i]=len(str)-1

  smallest=len(str)
  ma = len(str)
  mi = 0

  for i in range(len(str)):
    if str[i] in ar.keys():
      # reassign our pointer
      ar[str[i]]=i
      if smallest>max(ar.values())-min(ar.values()):
        ma = max(ar.values())
        mi = min(ar.values())
        smallest = ma-mi
  
  print(ma)
  print(mi)
  print(str[mi:ma+1])
  return str[mi:ma+1]

arr = ['x','y','z']
get_shortest_unique_substring(arr, "xyyzyzyx")


"""
arr = x, y, z

str = xyyzyzyx

1. look at sliding windows of str and see if we have
all the characters of arr 
- sliding window has to be at least width of len(arr)


solution:

dictionary key: the char
            value: 1

pointers for each character in arr

step through the example given
x - 0
y - 1 - 2
z - 3

(3- 0) + 1= 4

y - 4

greatest = 4, least x =0


5

z - 5
y - 6
x - 7

7-5 + 1 = 3

return str[5:7]


smallest = len(str)
smallest = max(pointer) - min(pointer)

pointer=[] index = same index as arr, that character is the one we're referring to
            value = the position of that character arr[i] where we see it currently in str

"""



  
