# My solution
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,16]
def myFunc(args):
  temp = 0
  start = args[0]
  end = args[-1]
  arr2 = []

  for x in range(end):
    arr2.append(x + 1)

  for x in range(len(args)):
    if(args[x] == arr2[x]):
      continue
    else:
      print(x+1)

print(myFunc([5]))
