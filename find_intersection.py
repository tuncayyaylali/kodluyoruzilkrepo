def FindIntersection(strArr):
  first = [i.split(", ") for i in strArr][0]
  second = [i.split(", ") for i in strArr][1]
  if len(first)>len(second):
    longest=len(first)
    longest_first=first
    longest_second=second
  else:
    longest=len(second)
    longest_first=second
    longest_second=first
  result=[]
  for i in longest_first:
    if i in longest_second:
      result.append(i)
  if len(result)!=0:
    return (",".join(result))
  else:
    return False
  # code goes here
  

# keep this function call here 
print(FindIntersection(input()))
