def FirstReverse(strParam):
  strParam=list(strParam)
  strParam.reverse()
  # code goes here
  return "".join(strParam)

# keep this function call here 
print(FirstReverse(input()))
